# G7_Prototype
Den endelige prototypen for gruppe G7 SE&amp;T 2021
Software Engineering and Testing – Gruppe 7 

 

Greit å få på plass struktur for dokumentasjonen tidlig  

Innhold  

Problemstillingen 

Domenet for applikasjonen  

Eksterne avhengigheter og avgrensede ansvarsområder  

Hva som er viktig med systemet  

Brukssituasjonen  

Story mapping og user stories  

Story mapping/Usecases 

Bruker(Auksjonær)/Kunde oppretter auksjon 

Auksjonær ønsker å få hjelp med logistikken tilknyttet sin auksjon 

Auksjonær ønsker sletting av sin auksjon 

Auksjonær ønsker detaljert auksjonsinformasjon tilknyttet et auksjon 

Auksjonær endrer auksjon 

Auksjonær ønsker å se en liste med auksjon 

Auksjonær ønsker å opprette nytt auksjon 

Delt Auksjonær ager ønsker å melde seg av et auksjon 

Aktiviteter og bruk av systemet/Forretningmodulene/Kjernefunksjonalitet 

Innlogging og autentisering  

Bestilling/Salg  

Ordre/leveranse  

Fakturering/Kreditering/Regnskap  

Klage/Reklamasjon/Lov og rett/Rettigheter  

Teknisk feil/Teknisk support (1., 2. og 3. linje)  

Teknisk massefeil (plattform, 3. linje)  

Automasjon av alle prosessene 

Bruk av systemet - Administrator  

Rapporter knyttet til systemet  

Kravspesifikasjonen av systemet  

Løsningen  

Overordnet beskrivelse av systemet Systemets bestanddeler  

Beskrivelse av arkitektur  

Forklaring av arkitekturtegningen  

Detaljert beskrivelse av systemet  

Innlogging og autentisering  

Ny bruker (ny person/ny juridisk enhet(organisasjon))  

Se tilgjengelige auksjoner 

Se pågående auksjoner 

Se historikk av alle auksjoner 

Budgiver melder seg på eksisterende auksjon 

Budgiver trekker seg fra eksisterende auksjon 

Bestille ny auksjon 

Aktivere auksjon 

Endre auksjon 

Reservere deltagerplasser på auksjon 

Kansellere reservasjoner av deltagerplasser  

Kansellere auksjon 

Gjenbruke en tidligere auksjon 

Detaljert Design  

Valg av teknologi og rammeverk  

Avanserte deler av systemet  

Vedlegg 1: Evaluering av gruppeprosjektet  

Organisering av gruppen: oppstart  

Tidsbruk  

Prototyping  

Arbeidsfordeling Og Evaluering 

Positive sider  

Negative sider  

Lærdom til senere prosjekter  

Prototypen  

Forklaring av prototypen  

Kjøring av prototypen  

Krav spesifikasjon: tenke modulært, velge ut det viktige i som skaper verdi(det helt sentrale i systemet), ha med krav som ikke blir implementert også  

Utkast for krav spec før møte på torsdag 

Funksjonelle krav: 

Auksjon systemet som er selve kjernen for programmet (X-Large) 

Kunne se høyeste bud i sanntid under auksjon 

Liste opp og filtrere antikviteter på salg 

Betalingssmetode/metoder med mulighet for å kreditere kjøp 

Brukerprofil/grensesnitt for å se antikviteter man har på salg 

Salgshistorikk 

Tanker om brukere: 

Bruker (abstraksjon): Auksjonær (privat/bedrift), Budgiver (privat/bedrift), Administrator(privat/bedrift), Auksjonshus, Foretak (bedrift) 

 

 

Ikke funksjonelle krav: 

 

Gruppeoppgaven (oppgaveteksten) 

Rundt om i Norge finnes det mange mindre butikker som driver med antikviteter og samlerobjekter. Disse har ofte et ønske om å kunne ha sin egen plattform der de kan auksjonere bort, selge og presentere varene de har på lager. 

I dette prosjektet skal dere lage en prosjektdokumentasjon og prototype for et produkt for en oppstartsbedrift. Denne oppstartsbedriften (Kunden deres) ønsker å få lagd en løsning der disse butikkene kan etablere sine egne plattformer for å løse disse behovene.  

Oppstartsbedriften har tidligere drevet med kjøp og salg, men har ingen egen IT-kompetanse. Idéen går ut på at oppstartsbedriften skal tilby plattformen sin som en abonnementsløsning og/eller som provisjonsbasert løsning (der Kunden som plattformeier tar en prosentandel av hvert salg) til sine brukere (antikvitets- og samlerbutikkene), mens sluttbrukerne (kundene til butikkene) kan f.eks. se, by på og kjøpe varer fra disse butikkene. 

Dere skal lage kjernesystemet i denne sfæren, og definere hvilke funksjoner som er påkrevd for at oppstartsbedriften (Kunden) får det systemet de ønsker. I tillegg skal det utvikles en prototype (et MVP som beskrevet i forelesningene) som implementerer et utvalg av funksjonene i systemet. Dere velger selv hvilke hovedfunksjoner dere vil vise fram i prototypen, så lenge prototypen har et visst omfang og vil kunne ha verdi for Kunden. Det skal også lages nødvendige, automatiserte tester som dokumenterer at prototypen tilfredsstiller de viktigste kravene som dere har avdekket og som blir beskrevet i dokumentasjonen dere skal produsere for systemet. 

Pass på at dere avgrenser hva systemet selv skal ha ansvar for og hva som håndteres av eksterne partnere. Visuell utforming (design) av brukergrensesnittet til applikasjonen er ikke viktig, men må være forståelig og hensiktsmessig for å vise fram det dere har lagd. Prototypens oppgave er å vise hvordan noe fungerer, ikke nødvendigvis hvordan det skal se ut. De automatiske testene dere leverer som en del av prototypen skal også vise hvordan funksjonene fungerer. Testene av prototypen skal i tillegg eksponere feilsituasjonene som kan oppstå under bruk av systemet, når systemet brukes slik gruppen har beskrevet i kravspesifikasjonen og modelleringen av systemet. 

Det er viktig at dere passer på å dokumentere eksterne avhengigheter i systemet, dvs. der systemet må prate med systemer fra andre tjenesteleverandører (f.eks. betalingsløsning). Dere skal ikke integrere mot noen eksterne leverandører i prototypen, men bør skrive små “stubs” som gir dere muligheten til å teste funksjonaliteter som avhenger av dem. 

Vi oppfordrer dere til å følge en mest mulig Agile arbeidsform, der spesifikasjonen, produktet og koden (m/tester) utvikler seg sammen gjennom hele prosjektperioden og dere avgjør hva dere skal jobbe med og levere til prosjektet i “sprinter”. Dere bør ha korte “standups” et par ganger i uka for å sørge for kontinuerlig framdrift i prosjektet. 

Hver gruppe får tilbud om to runder med femten minutters veiledning fra faglærer. Dette annonseres via Canvas og det er gruppens eget ansvar å booke seg inn på et av de tilgjengelige tidspunktene som annonseres. Første veiledning vil være tidlig i prosjektet, mens andre veiledning vil være omtrent midtveis. Det er viktig at dere forbereder dere til veiledningsmøtene slik at dere vet hva dere skal spørre om og hva dere trenger hjelp med. Dere kan gjerne sende inn spesifikt hva dere vil ha tilbakemelding om på forhånd. Det forventes at alle gruppemedlemmene møter på begge veiledningene. 

Følg med på Canvas for presiseringer og svar på gjentagende spørsmål. Les “Tips til prosjektdokumentasjonen og prototypen” på Canvas for ytterligere presiseringer og tips til det som skal leveres. 

 
Innlevering 

Det skal leveres en prosjektdokumentasjon som forklarer problemstillingen og den helhetlige løsningen dere foreslår for problemstillingen, slik at Kunden som beskrevet ovenfor og eksterne partnere kan lese gjennom dokumentasjonen og forstå problemet, hva som skal utvikles og hva som er viktig med systemet som utvikles. Husk at dokumentasjonen skal være forståelig for personer uten inngående kunnskap om fagområdet eller programmering. 

Kravene til systemet og systemet som helhet skal være dokumentert på et slikt nivå at dokumentasjonen kan sendes til eksterne selskap som kan utvikle, teste og evaluere systemet i samarbeid med produkteier og oppdragsgiver. Hvert krav skal inneholde gruppens eget estimat for utviklingsomfang og forretningsnytte i henhold til “T-Shirt sizing”-estimeringsmetoden (Small/Medium/Large/X-Large). 

Gruppen skal levere en fungerende prototype som omfatter de viktigste delene av det foreslåtte systemet. Prototypen skal inneholde nødvendige tester for å vise at kravene i dokumentasjonen er oppfylt. 

Prototypen skal være robust og skal kunne gi verdi til Kunden - det vil si at det må være faktiske funksjoner som er implementert som vil kunne gi en form for verdi slik de er nå. Prototypen skal ha persistent lagring, slik at applikasjonen kan lukkes og startes opp igjen med samme innhold som tidligere. 

Det er fritt valg av programmeringsspråk og ev. rammeverk, men dere må sørge for at det er enkelt for Kunden, med sin minimale IT-bakgrunn, å få prototypen og tilhørende tester til å kjøre. 

Kildekoden til prototypen skal leveres som et Git-repository som viser utviklingen av prototypen over prosjektperioden. Pass på at `.git`-mappen blir med i innleveringen deres, og at dere har committet alle endringene før dere leverer. Det forventes at dere benytter Git aktivt under utviklingen av prototypen. Sørg for at det er beskrevet hvordan en person uten dyptgående IT-kunnskap kan bygge, kjøre og teste prototypen deres. Avhengigheter i applikasjonen deres skal kunne installeres automatisk ved hjelp av et pakkesystem for språket eller rammeverket dere benytter (f.eks. maven eller gradle om dere bruker Java, pip eller poetry for Python). 

Merk at prosjektoppgaven skal inneholde minst to forskjellige diagram fra hver av deltakerne i gruppa. Disse diagrammene kan være enten dataflytdiagram, sekvensdiagram, tilstandsdiagram eller aktivitetsdiagram. Diagrammene skal vise ulike funksjoner i systemet. Hver deltaker i gruppa skal også gjøre en individuell levering som består av et enkelt dokument som inneholder en beskrivelse av den valgte måten å organisere gruppa på, arbeidsfordeling og av hvem som har gjort hva. Fokus skal ligge på hvordan organisasjonen av arbeidet i gruppa fungerte, både positive sider, negative sider, arbeidsfordeling og lærdom til senere prosjekter. 

Disse vedleggene skal inkluderes samlet i den felles gruppeinnleveringen.  

Dokumentene i innleveringen skal leveres som PDF-filer, og hele prosjektet (prosjektdokumentasjon, prototype og vedlegg) skal leveres samlet for gruppa som en .zip-fil i Inspera. Det er kun det som er inkludert i gruppeinnleveringen i Inspera som blir tatt med i vurderingen (så ingen eksterne git-repositories, etc.). 

 

Evaluering 

Innleveringen evalueres ut fra: 

● egnethet for å kunne ta i bruk den foreslåtte løsningen 

● kvalitet på prototypen 

● testing av funksjonene i prototypen opp mot krav 

● egnethet og kvalitet på prosjektdokumentasjonen 

Gruppeprosjektet teller 45%. Det gis individuell karakter A-F (se emnebeskrivelsen for mer informasjon). 

Ikke-funksjonelle krav: 

Lag use case-diagrammer som viser hva en bruker og en administrator kan gjøre i en slik tjeneste. 

Beskriv tre funksjonelle krav som stilles til systemet som en følge av use case-diagrammene. Bryt kravene opp i underkrav der det er nødvendig. 

Beskriv minst ett ikke-funksjonelt krav. 

Lag et sekvensdiagram som viser hvordan flyten mellom hvert lag i systemet kan være når en bruker ønsker å betale for innhold på en slik tjeneste. Anta at kunden betaler med et kredittkort. Bruk verb eller metodenavn som tekst over hver pil. 

Tenk gjennom hvilke feilsituasjoner som kan oppstå og lag et sekvensdiagram som viser en slik situasjon. 

 

 

Diagrammer: 

OBS! Vi limer dette inn fra PlantUML fra PyCharm-prosjektet når det nærmer seg slutten, før vi skal ferdigstille dette dokumentet. Dette for å sikre at diagrammene er mest mulig oppdaterte og riktige før vi flytter bilder derfra til dette dokumentet. 

 

Kilder: 

Kravspesifikasjon: 

https://www.stxnext.com/blog/software-product-requirements-high-level-project-specifications-guide 

https://www.iso.org/standard/72189.html 

https://www.geeksforgeeks.org/software-engineering-software-product/ 

https://en.wikipedia.org/wiki/Software_requirements_specification 

https://www.researchgate.net/publication/229017168_Requirements_Engineering_for_Software_Product_Lines 

https://relevant.software/blog/software-requirements-specification-srs-document/ 

https://www.javatpoint.com/software-requirement-specifications 

Mocking: 

https://docs.python.org/3/library/unittest.mock-examples.html 

 

Videoer: 

An introduction to Requirements Engineering 



Requirements Engineering Processes 



Requirements engineering challenges 



 

 

Oppgaven: 

https://hiof.instructure.com/courses/5120/files?preview=968260 

 
