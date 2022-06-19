from songline import Sendline # Uncle-engineer pip install songline
token = 'bG2O8AH9pntUNBkWUtnNHDeIzlO00CKUxxT84KFGw2o' # ต้องไป Generate TOKEN ก่อน (1 Token ส่งได้ 1 กลุ่ม)
messenger = Sendline(token) 
#messenger.sendtext('hello world TER')
#messenger.sticker(620, 4)
messenger.sendimage('https://i.pinimg.com/originals/d8/36/b7/d836b748cfd1fdeb0b1ff12f31e2cdbe.jpg')