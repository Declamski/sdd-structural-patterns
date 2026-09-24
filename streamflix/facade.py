
from .payments import PaymentProcessor
from .catalog import Video


class StreamingFacade:
    """
    Simplified entry point for the mobile/web client: it never talks to
    payment processors or videos directly, only to this facade.
    """

    def __init__(self, payment_processor: PaymentProcessor):
      # TODO: store the payment processor and start unsubscribed
      self._subscribed = False
      self._payment_processor = payment_processor

    def subscribe(self, monthly_fee: float) -> str:
      self._subscribed = True
      return self._payment_processor.pay(monthly_fee)

    def watch(self, video: Video) -> str:
      if self._subscribed == False:
         raise PermissionError("subscription required")
      return video.play()
