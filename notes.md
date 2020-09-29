

This deploys 2 lambdas that can be called via api gateway:

1. extractive summarizer: `lambda_function.py` (api: `POST` `/v1/public/text-summarizer`)
- input body: 

```json
{
    "text": "US President Donald Trump on Wednesday declined to commit to a peaceful transfer of power if he loses the November 3 presidential election.\n\n“We’re going to have to see what happens,” Trump said at a news conference, responding to a question about whether he’d commit to a peaceful transfer of power. “You know that I’ve been complaining very strongly about the ballots, and the ballots are a disaster.”\n\nTrump has been pressing a monthslong campaign against mail-in voting this November by tweeting and speaking out critically about the practice. More states are encouraging mail-in voting to keep voters safe amid the coronavirus pandemic.\n\nThe president, who uses mail-in voting himself, has tried to distinguish between states that automatically send mail ballots to all registered voters and those, like Florida, that send them only to voters who request a mail ballot.\n\nTrump has baselessly claimed widespread mail voting will lead to massive fraud. The five states that routinely send mail ballots to all voters have seen no significant fraud.\n\nFacebook announced it will not accept political ads that seek to claim victory before the results of the 2020 US election are declared, a company spokesman tweeted on Wednesday.\n\nThe move expands the company’s plans, announced earlier this month, to stop accepting new political ads in the week before the election. At the time, Facebook said political advertisers could resume creating new ads after Election Day.\n\nDemocrats have warned of a “red mirage” on election night, citing expected delays in counting a record number of mail-in ballots this year, and raised concerns that Trump could use Facebook to convince people he had won.",
    "sentences": 3
}
```

- uses `sumy` lib

2. abstractive summarizer: `lambda_function_bert.py` (api: `POST` `/v1/public/text-summarizer-bert`)

```json
{
    "text": "US President Donald Trump on Wednesday declined to commit to a peaceful transfer of power if he loses the November 3 presidential election.\n\n“We’re going to have to see what happens,” Trump said at a news conference, responding to a question about whether he’d commit to a peaceful transfer of power. “You know that I’ve been complaining very strongly about the ballots, and the ballots are a disaster.”\n\nTrump has been pressing a monthslong campaign against mail-in voting this November by tweeting and speaking out critically about the practice. More states are encouraging mail-in voting to keep voters safe amid the coronavirus pandemic.\n\nThe president, who uses mail-in voting himself, has tried to distinguish between states that automatically send mail ballots to all registered voters and those, like Florida, that send them only to voters who request a mail ballot.\n\nTrump has baselessly claimed widespread mail voting will lead to massive fraud. The five states that routinely send mail ballots to all voters have seen no significant fraud.\n\nFacebook announced it will not accept political ads that seek to claim victory before the results of the 2020 US election are declared, a company spokesman tweeted on Wednesday.\n\nThe move expands the company’s plans, announced earlier this month, to stop accepting new political ads in the week before the election. At the time, Facebook said political advertisers could resume creating new ads after Election Day.\n\nDemocrats have warned of a “red mirage” on election night, citing expected delays in counting a record number of mail-in ballots this year, and raised concerns that Trump could use Facebook to convince people he had won.",
}
```

- this lambda simply calls the huggingface api using `hfapi`, hitting the `summarization` endpoint for model: `sshleifer/distilbart-cnn-12-6`
- TODO: refactor this lambda to actually do summarization with this model emulating what the hfapi summarization endpoint does:

Here's the hfapi calling the api:

https://github.com/huggingface/hfapi/blob/master/hfapi/__init__.py

This is the model: 

https://huggingface.co/sshleifer/distilbart-cnn-12-6

This is how the above page says to use the model directly with teh huggingface transformers lib:

```
from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")

model = AutoModelWithLMHead.from_pretrained("sshleifer/distilbart-cnn-12-6")
```

I went with this approach based on this comment:

https://github.com/huggingface/transformers/issues/5303#issuecomment-650366831

(I was following this article, but the above comment clarified that there are more accurate abstractive models: https://towardsdatascience.com/summarization-has-gotten-commoditized-thanks-to-bert-9bb73f2d6922)

Which should be able to follow this `seq2seq` instructions:

https://github.com/huggingface/transformers/tree/master/examples/seq2seq

specifially this hsould work (but need to find out exactly what is running in the huggingface api):

https://github.com/huggingface/transformers/tree/master/examples/seq2seq#evaluation-commands


This article and accompaniying github repo may help:

https://www.philschmid.de/serverless-bert-with-huggingface-and-aws-lambda
https://github.com/philschmid/serverless-bert-with-huggingface-aws-lambda
