import nltk
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pylab as plt
from konlpy.tag import Twitter
from PIL import Image
import PIL
import random
from PyInstaller.utils.hooks import collect_data_files
from tkinter import *
from tkinter.filedialog import *
print("="*30, "라이브러리 임포트 완료", "="*30)

root = Tk()
root.title("WordCloud")
root.geometry("640x400+100+100")
root.resizable(False, False)
print("="*30, "윈도우 생성", "="*30)

name = ""
background = None
stopwords = None


def grey_color(word, font_size, position, orientation, random_state=None, **kwargs):
	return 'hsl(0, 0%%, %d%%)' % random.randint(80, 100)


print("="*30, "폰트 색 변경 함수 생성", "="*30)


# 파일 경로 받은 후 전역 변수 name에 저장
def get_text_path():
	global name
	name = askopenfilename()
	print(name)


print("="*30, "텍스트 파일 업로드 함수 생성", "="*30)


def get_img_path():
	global background, stopwords
	file = askopenfilename()
	background = np.array(PIL.Image.open(file))
	print(background)


print("="*30, "이미지 업로드 함수 생성", "="*30)


def make_wordcould():
	global background, stopwords
	text = open(name, encoding='utf-8').read()
	wc = WordCloud(background_color='white', margin=5, mask=background,
	               max_words=2000, stopwords=stopwords, random_state=1).generate(text)

	default_colors = wc.to_array()
	plt.figure(figsize=(10, 10))
	plt.imshow(wc, interpolation='bilinear')
	# plt.imshow(wc.recolor(color_func=grey_color, random_state=3), interpolation='bilinear')
	plt.axis('off')
	plt.show()


print("="*30, "영문 워드클라우드 함수 생성", "="*30)


def make_korean():
	global background, stopwords
	text = open(name, encoding='utf-8').read()
	t = Twitter()
	token = t.nouns(text)
	count_voca = nltk.Text(token, name="단어카운팅")
	count_voca.vocab()
	voca = count_voca.vocab().most_common(150)
	font ="/usr/share/fonts/NanumFont/NanumGothicBold.ttf"
	wordcloud = WordCloud(font_path=font, max_words=2000,
	                      relative_scaling=0.2,
	                      background_color="white", mask=background).generate_from_frequencies(dict(voca))
	plt.figure(figsize=(12, 12))
	plt.imshow(wordcloud, interpolation='bilinear')
	# plt.imshow(wordcloud.recolor(color_func=grey_color, random_state=3), interpolation='bilinear')
	plt.axis('off')
	plt.show()


print("="*30, "한글 워드클라우드 함수 생성", "="*30)

# UI 부품 추가
Bt1 = Button(root, text = "텍스트 파일 업로드", command = get_text_path, font="/usr/share/fonts/NanumFont/NanumGothicBold.ttf")
Bt1.place(x = 150, y = 60, width = 160, height = 50)

Bt2 = Button(root, text = "영문 전용\n워드 클라우드 만들기", command = make_wordcould, font="/usr/share/fonts/NanumFont/NanumGothicBold.ttf")
Bt2.place(x = 150, y = 120, width = 160, height = 50)

Bt3 = Button(root, text = "한글 전용\n워드 클라우드 만들기", command = make_korean, font="/usr/share/fonts/NanumFont/NanumGothicBold.ttf")
Bt3.place(x = 320, y = 120, width = 170, height = 50)

Bt4 = Button(root, text = "워드클라우드\n 실루엣 이미지 업로드", command = get_img_path, font="/usr/share/fonts/NanumFont/NanumGothicBold.ttf")
Bt4.place(x = 320, y =60, width=170, height = 50)

LB1 = Label(root, text = "* 주의 사항 *\n 워드 클라우드 작업 시 실루엣 이미지를 사용하지 않을 경우\n 사각형 모양으로 기본 세팅됩니다.")
LB1.config(font=("/usr/share/fonts/NanumFont/NanumGothicBold.ttf", 10))
LB1.place(x = 160, y = 200, width = 330, height = 50)

LB2 = Label(root, text = "WORD CLOUD 생성 프로그램")
LB2.config(font=("/usr/share/fonts/NanumFont/NanumGothicBold.ttf", 20))
LB2.place(x = 30, y = 10, width = 600, height = 30)

print("="*30, "버튼 및 레이블 생성 완료", "="*30)


root.mainloop()

