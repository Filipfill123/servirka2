from dialog import SpeechCloudWS, Dialog, ABNF_INLINE
import random
import asyncio
import logging
from pprint import pprint, pformat
from collections import Counter

class Mocniny(Dialog):

    async def main(self):
        HLAS = "Iva30"


        await self.synthesize_and_wait(text="Dobrý den, jsem vaše virtuální mocnina Karel. Zadejte číslo.", voice=HLAS)
        while True:
            #self.sc.led_breath_slow()
            message = await self.sc.dm_send_message()
            number = int(message["data"]["number"])
            print("number: ", number)
            number_squared = str(number*number)
            await self.synthesize_and_wait(text=number_squared, voice=HLAS)
            logging.info(msg=number)
            #self.sc.led_off()


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)-10s %(message)s', level=logging.DEBUG)

    SpeechCloudWS.run(Mocniny, address="0.0.0.0", port=8888, static_path="./static", static_route="/(.*)")
