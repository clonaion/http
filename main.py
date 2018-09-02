import urllib2
import datetime
import time
import random
from fake_useragent import UserAgent


def main():
    URLS = [
        "https://bindings-martins.herokuapp.com",  "https://jessicas-invectives.herokuapp.com",   "https://lanes-enforces.herokuapp.com",    "https://oboes-troweling.herokuapp.com",   "https://bane-intercontinental.herokuapp.com",
        "https://antiquarians-stalwarts.herokuapp.com",    "https://attributes-equivocated.herokuapp.com",    "https://christi-dissented.herokuapp.com", "https://deprograms-lapidary.herokuapp.com",   "https://grammars-ruckuses.herokuapp.com",
        "https://roscoe-english.herokuapp.com",    "https://woefullest-locke.herokuapp.com",  "https://shepherded-abrams.herokuapp.com", "https://brutalities-perched.herokuapp.com",   "https://rental-safaried.herokuapp.com",
        "https://antics-handcarts.herokuapp.com",  "https://churchmans-cas.herokuapp.com",    "https://innovating-largesses.herokuapp.com",  "https://racy-cartoons.herokuapp.com", "https://slues-pockmark.herokuapp.com",
        "https://albacores-arequipa.herokuapp.com",    "https://buttress-lurching.herokuapp.com", "https://hunchbacks-kerensky.herokuapp.com",   "https://pugnacious-byproducts.herokuapp.com", "https://putty-waterspouts.herokuapp.com",
        "https://breach-exhibiting.herokuapp.com", "https://earthward-peaches.herokuapp.com", "https://hatreds-pediments.herokuapp.com", "https://indescribable-moppets.herokuapp.com", "https://unhealthiest-fibs.herokuapp.com",
        "https://actress-bunches.herokuapp.com",   "https://barcelona-ferlinghetti.herokuapp.com",    "https://burks-microsoft.herokuapp.com",   "https://frailties-quailing.herokuapp.com",    "https://yvonne-hesitate.herokuapp.com",
        "https://courthouses-bedpans.herokuapp.com",   "https://moons-americanizations.herokuapp.com",    "https://retorting-emanuels.herokuapp.com",    "https://retouch-kampucheas.herokuapp.com",    "https://workmans-complete.herokuapp.com",
        "https://boles-debonairly.herokuapp.com",  "https://cesiums-misidentify.herokuapp.com",   "https://inconsiderateness-dig.herokuapp.com", "https://narcissism-pucker.herokuapp.com", "https://peaceably-wants.herokuapp.com",
        "https://cervantes-wistarias.herokuapp.com",   "https://cushier-castanets.herokuapp.com", "https://deplored-persuasions.herokuapp.com",  "https://gristlier-craw.herokuapp.com",    "https://kits-glaxos.herokuapp.com",
        "https://crimson-teris.herokuapp.com", "https://crossest-disputations.herokuapp.com", "https://internationalisms-spoonerism.herokuapp.com",  "https://reproductions-saloon.herokuapp.com",  "https://unit-dictate.herokuapp.com",
        "https://discarding-monosyllabic.herokuapp.com",   "https://footwork-proviso.herokuapp.com",  "https://furling-springsteens.herokuapp.com",  "https://punjab-plagiarisms.herokuapp.com",    "https://zeroing-accustoms.herokuapp.com",
        "https://contributions-passion.herokuapp.com", "https://mimicking-interrelating.herokuapp.com",   "https://sheriff-canada.herokuapp.com",    "https://specific-unhesitating.herokuapp.com", "https://takingss-thinking.herokuapp.com",
        "https://campers-unsatisfied.herokuapp.com",   "https://hippocratess-worsen.herokuapp.com",   "https://internationals-betided.herokuapp.com",    "https://myrtles-dolts.herokuapp.com", "https://presumptions-chesters.herokuapp.com",
        "https://galvanic-paupers.herokuapp.com",  "https://legends-apices.herokuapp.com",    "https://percussions-inborn.herokuapp.com",    "https://philosophized-knitted.herokuapp.com", "https://viruses-disembowels.herokuapp.com",
        "https://adore-parcheesis.herokuapp.com",  "https://crimsoning-deserving.herokuapp.com",  "https://frs-moleskin.herokuapp.com",  "https://households-brisker.herokuapp.com",    "https://icings-incitements.herokuapp.com",
        "https://attributively-dissemble.herokuapp.com",   "https://enumerating-cockerels.herokuapp.com", "https://ispells-naughtiest.herokuapp.com",    "https://ophelia-socking.herokuapp.com",   "https://unintentionally-norsemen.herokuapp.com",
        "https://adjuration-distentions.herokuapp.com",    "https://aliased-blinders.herokuapp.com",  "https://chainsawing-crowns.herokuapp.com",    "https://emulator-typefaces.herokuapp.com",    "https://handrail-rechecking.herokuapp.com",
    ]

    ua = UserAgent(cache=False)

    while True:
        for url in URLS:
            contents = "empty"

            try:
                request = urllib2.build_opener()
                request.addheaders = [('User-Agent', ua.random)]
                response = request.open(url)
                contents = response.read()

                if response.getcode() is not 200:
                    raise "Status Code " + str(response.getcode())
                if contents != "YES":
                    raise "Nnet down"

                print("[{0}] INFO: {1} - ok".format(datetime.datetime.now(), url))

            except Exception as e:
                print("[{0}] ERROR getting {1}: {2} - {3}".format(datetime.datetime.now(), url, e, contents))

        minutes = random.randint(10,20)
        print("[{0}] INFO: sleeping for {1} minutes...".format(datetime.datetime.now(), minutes))
        time.sleep(minutes * 60)


if __name__ == "__main__":
    main()
