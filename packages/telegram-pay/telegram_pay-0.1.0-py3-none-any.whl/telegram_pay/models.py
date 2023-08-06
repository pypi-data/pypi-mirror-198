from __future__ import annotations
from typing import Optional
from decimal import Decimal
from datetime import datetime
    
import aiohttp
from pydantic import BaseModel

from .enums import Currency, Interval, SubscriptionStatus, TransactionStatus

class TelegramPay(BaseModel):
    url = 'https://api.pay.4u.studio/'
    shop_id: str
    shop_token: str

    async def make_request(self, endpoint: str, params: dict = None) -> dict:
        headers = {'X-API-Key': self.shop_token}
        
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url + endpoint, params=params, headers=headers) as response:
                response.raise_for_status()
                return await response.json()
            
    async def get_user_subscription(self, user_id: int, subscription_id: str) -> Subscription:
        endpoint = "subscriptions/search"
        params = {
            "user_id": user_id,
            "subscription_id": subscription_id
        }
        subscription_json = await self.make_request(endpoint, params)

        if len(subscription_json) > 0:
            subscription_json[0]["exists"] = True
            subscription_json[0]["client"] = self
            return Subscription(**(subscription_json[0]))
        
        return Subscription(client=self, id=subscription_id, exists=False, user_id=user_id)

    async def cancel_subscription(self, subscription_unique_id: str):
        endpoint = f"subscriptions/{subscription_unique_id}/cancel"
        return await self.make_request(endpoint)

class Subscription(BaseModel):
    client: TelegramPay
    subscription_id: str
    exists: bool
    test_mode: bool
    user_id: int
    unique_id: Optional[str]
    valid_until: Optional[datetime]
    amount: Optional[Decimal]
    currency: Optional[Currency]
    interval: Optional[Interval]
    status: Optional[SubscriptionStatus]
    description: Optional[str]
    start_date: Optional[datetime]

    @property
    def valid(self) -> bool:
        return self.exists and datetime.now() < self.valid_until
    
    @property
    def expired(self) -> bool:
        return self.exists and self.status in [SubscriptionStatus.REJECTED,
                                               SubscriptionStatus.PAST_DUE,
                                               SubscriptionStatus.EXPIRED]
    
    @property
    def canceled(self) -> bool:
        return self.exists and self.status == SubscriptionStatus.CANCELLED
    
    @property
    def cancellable(self):
        return self.exists and self.status in [SubscriptionStatus.ACTIVE, 
                                               SubscriptionStatus.PAST_DUE]
    
    async def cancel(self):
        if self.cancellable:
            await self.client.cancel_subscription(self.unique_id)