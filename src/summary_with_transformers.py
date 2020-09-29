# pip install torch torchvision
# pip install transformers


# from transformers import AutoTokenizer, AutoModelWithLMHead

# tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")

# model = AutoModelWithLMHead.from_pretrained("sshleifer/distilbart-cnn-12-6")



# pip install git+https://github.com/huggingface/hfapi/

import hfapi
client = hfapi.Client()

result = client.summarization(
  # "Good Afternoon Jan,\r\n\r\n \r\n\r\nWe are very excited to assist you in the purchase of your first home! Understanding the process can be a daunting task however, we are here to help you every step of the way and will answer any questions you have.\r\n\r\n \r\n\r\nSome things to get started..\r\n\r\n \r\n\r\nIf you are purchasing this property with a mortgage you can now contact your provider and provide them with the relevant information to get your loan approved.\r\n\r\nYou will be required to pay a 10% deposit next week. This will be payable to me and I will hold the funds until settlement.\r\n\r\nSettlements are now done online (no need to leave your house!). This is done on a platform called PEXA and I have included some information below on what this is.\r\n\r\nI will forward you a copy of the contract in the next 24hours for your signature. You are able to electronically sign using InfoTracks SignIt.\r\n\r\nKind Regards,\r\n\r\n \r\n\r\nAli Moussa Conveyancer",
  # "Hi Ali,\r\n\r\nThats awesome. I'll try to get the deposit in to you as soon as possible. Can I please have a receipt and a copy of the signed contract for my broker?\r\n\r\nThank you so much for your help.\r\n\r\nJay Robins - signing out.",
  "US President Donald Trump on Wednesday declined to commit to a peaceful transfer of power if he loses the November 3 presidential election.\n\n“We’re going to have to see what happens,” Trump said at a news conference, responding to a question about whether he’d commit to a peaceful transfer of power. “You know that I’ve been complaining very strongly about the ballots, and the ballots are a disaster.”\n\nTrump has been pressing a monthslong campaign against mail-in voting this November by tweeting and speaking out critically about the practice. More states are encouraging mail-in voting to keep voters safe amid the coronavirus pandemic.\n\nThe president, who uses mail-in voting himself, has tried to distinguish between states that automatically send mail ballots to all registered voters and those, like Florida, that send them only to voters who request a mail ballot.\n\nTrump has baselessly claimed widespread mail voting will lead to massive fraud. The five states that routinely send mail ballots to all voters have seen no significant fraud.\n\nFacebook announced it will not accept political ads that seek to claim victory before the results of the 2020 US election are declared, a company spokesman tweeted on Wednesday.\n\nThe move expands the company’s plans, announced earlier this month, to stop accepting new political ads in the week before the election. At the time, Facebook said political advertisers could resume creating new ads after Election Day.\n\nDemocrats have warned of a “red mirage” on election night, citing expected delays in counting a record number of mail-in ballots this year, and raised concerns that Trump could use Facebook to convince people he had won.",
  model="sshleifer/distilbart-cnn-12-6"
)

print('result:', result)