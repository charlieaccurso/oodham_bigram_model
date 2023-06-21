# oodham_bigram_model
Simple bigram model for small dataset of Tohono O'odham sentences.
This bigram model generates novel sentences based on bigram probabilities. Some are correct and others are ungrammatical.
Ungrammaticity arises from the model's inability to capture subject-verb number dependencies.

Sentences from Ofelia Zepeda's _A Papago Grammar_.

# Sample outputs include:
ñeok </s> "speaks" (sentence fragment)
hegai cehia 'o hegam 'u'uwĭ </s> "this girl aux these women" (ungrammatical)
'idam cecia 'o ṣoañ </s> "these girls are crying" (correct)
'i:da 'uwĭ </s> "this woman" (grammatical fragment)
pi ṣoañ </s> "not crying" (ungrammatical, missing aux)

pi 'o cicwi hegai 'uwĭ </s> "this woman isn't playing" (correct)
hegai 'o'odham 'o cicwi </s> "that person is playing" (correct)
pi ñeok </s> "Not speaking" (ungrammatical, missing aux)
'i:da 'o'odham </s> "this person" (grammatical fragment)
pi 'o pi 'o hegam 'o'odham </s> "not aux not aux these people" (ungrammatical)

hegam 'o'odham </s> "these people" (grammatical fragment)
'i:da 'o'odham </s> "this person" (grammatical fragment)
cicpkan </s> "working" (missing aux)
hegai 'uwĭ </s> "this woman" (grammatical fragment)
'i:da 'ali 'o pi 'o ñeok 'i:da 'o'odham </s> "this child aux not speaking this person" (ungrammatical)

# Some outputs are quite long:
'idam cecoj 'o 'i:da 'o'odham 'o ñeñok 'o ñeñok 'idam cecoj </s> "these boys aux this person speaking speaking these boys" (ungrammatical)
pi 'o pi 'o pi 'o pi 'o ñeñok 'o hegam 'a'al 'o hegam 'o'odham </s> "not aux not aux not aux not aux speaking aux these babies aux these people" (ungrammatical)
