from dialog import SpeechCloudWS, Dialog, ABNF_INLINE
import random
import asyncio
import logging
from pprint import pprint, pformat
from collections import Counter

class Mocniny(Dialog):

    async def main(self):
        HLAS = "Iva30"
        dict_of_numbers = {"jedna":1, "dva": 2, "tři": 3, "čtyři": 4, "pět": 5, "šest": 6, "sedm": 7, "osm": 8, "devět": 9, "deset": 10}

        await self.synthesize_and_wait(text="Dobrý den. Zadejte číslo od jedné do deseti, nebo zmáčkněte tlačítko ASR a řekněte číslo.", voice=HLAS)
        while True:
            #self.sc.led_breath_slow()
            message = await self.sc.dm_send_message()
            data = message["data"]
            if data:
                result = data["result"]
                if result in dict_of_numbers.keys:
                    number = dict_of_numbers[result]
                    number_squared = str(number*number)
                    await self.synthesize_and_wait(text=f'Druhá mocnina čísla {number} je {number_squared}', voice=HLAS)
                    #logging.info(msg=number)
                elif result in dict_of_numbers.values:
                    number = result
                    number_squared = str(number*number)
                    await self.synthesize_and_wait(text=f'Druhá mocnina čísla {number} je {number_squared}', voice=HLAS)
                else:
                    await self.synthesize_and_wait(text=f'Omluvám se, asi jsem Vám nerozuměla.', voice=HLAS)

            else: 
                await self.synthesize_and_wait(text="Slyším a poslouchám.", voice=HLAS)
            #self.sc.led_off()


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)-10s %(message)s', level=logging.DEBUG)

    SpeechCloudWS.run(Mocniny, address="0.0.0.0", port=8888, static_path="./static", static_route="/(.*)")
