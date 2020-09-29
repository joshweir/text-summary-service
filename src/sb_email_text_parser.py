import re

class SbEmailTextParser:

  def __init__(self):
    print('init..')

  def __call__(self, text):
    result = self.remove_smokeball_reference(
      self.remove_email_header_metadata(
        self.extract_latest_response(
          text
        )
      )
    )
    
    return result

  def extract_latest_response(self, text):
    parts = re.split(r'\sOn\s[^\n\r]+\<mailto:[^\n\r]+>[^\n\r]+\swrote:\s{0,1}', text)
    return parts[0]

  def remove_email_header_metadata(self, text):
    parts = re.split(r'\sFrom:\s*[^\s]*.+\s{1}To:\s*[^\s]+.+\s{1}', text)
    if len(parts) > 1:
      parts.pop(0)
      return ' '.join(parts)
    return text

  def remove_smokeball_reference(self, text):
    return re.sub(r'\sSmokeball Reference:\s*[^\s]+', ' ', text)


if __name__ == '__main__':
  email_text_parser = SbEmailTextParser()
  result = email_text_parser(
    "First Home Purchase\r\nFrom: Ali Moussa \r\nTo:  jay.robins84@gmail.com\r\nGood Afternoon Jan,\r\n\r\n \r\n\r\nWe are very excited to assist you in the purchase of your first home! Understanding the process can be a daunting task however, we are here to help you every step of the way and will answer any questions you have.\r\n\r\n \r\n\r\nSome things to get started..\r\n\r\n \r\n\r\nIf you are purchasing this property with a mortgage you can now contact your provider and provide them with the relevant information to get your loan approved.\r\n\r\nYou will be required to pay a 10% deposit next week. This will be payable to me and I will hold the funds until settlement.\r\n\r\nSettlements are now done online (no need to leave your house!). This is done on a platform called PEXA and I have included some information below on what this is.\r\n\r\nI will forward you a copy of the contract in the next 24hours for your signature. You are able to electronically sign using InfoTrack's \"SignIt\".\r\n\r\nKind Regards,\r\n\r\n \r\n\r\nAli Moussa Conveyancer\r\n\r\nSmokeball Reference: a19becc0-904f-4940-ac65-bcd4f6bdff8b/bde10b74-ae8c-4414-8d7f-63bccdbca0d5.\r\n\r\n"
  )
  print('result:', result)
  print()
  print()
  result2 = email_text_parser(
    "Re: Email to Jay\r\nFrom: Jay Robins jay.robins84@gmail.com\r\nTo: Ali Moussa ali.moussa@smokeball.com\r\nHi Ali,\r\n\r\nThats awesome. I'll try to get the deposit in to you as soon as possible. Can I please have a receipt and a copy of the signed contract for my broker?\r\n\r\nThank you so much for your help.\r\n\r\nJay Robins - signing out.\r\n\r\n\r\nOn Thu, Sep 24, 2020 at 4:54 PM Ali Moussa <ali.moussa@smokeball.com <mailto:ali.moussa@smokeball.com> > wrote:\r\n\r\n\r\n\tGood Afternoon Jan,\r\n\r\n\t\r\n\r\n\t \r\n\r\n\tWe are very excited to assist you in the purchase of your first home! Understanding the process can be a daunting task however, we are here to help you every step of the way and will answer any questions you have.\r\n\r\n\t\r\n\r\n\t \r\n\r\n\tSome things to get started..\r\n\r\n\t \r\n\r\n\tIf you are purchasing this property with a mortgage you can now contact your provider and provide them with the relevant information to get your loan approved.\r\n\r\n\tYou will be required to pay a 10% deposit next week. This will be payable to me and I will hold the funds until settlement.\r\n\r\n\tSettlements are now done online (no need to leave your house!). This is done on a platform called PEXA and I have included some information below on what this is.\r\n\r\n\tI will forward you a copy of the contract in the next 24hours for your signature. You are able to electronically sign using InfoTracks SignIt.\r\n\r\n\t\r\n\r\n\tKind Regards,\r\n\r\n\t \r\n\r\n\tAli Moussa Conveyancer\r\n\r\n\tSmokeball Reference: a19becc0-904f-4940-ac65-bcd4f6bdff8b/6f748bef-d493-4f8f-b96f-bedecc912673. \r\n\r\n\r\n"
  )
  print('result2:', result2)