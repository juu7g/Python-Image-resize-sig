# Python-Image-resize-sig


## 概要 Description
文字透かし付き画像サイズ変換ツール  

Python の pillow を使用して画像サイズを変更し、文字透かしを入れられるツールです。  
You can resize the image and add a text watermark to the image by Python pillow.  

## 特徴 Features

- アスペクト比固定で縦か横のサイズを指定してサイズ変更します  
	Resize by specifying the vertical or horizontal size with a fixed aspect ratio
- 画像は exe にドラッグアンドドロップするかファイルダイアログで選択します  
	Select the image by dragging and dropping it to the exe or select it in the file dialog
- Exif情報を残すか消すか選択できます  
	You can choose to keep or erase Exif information
- 画像に文字で透かしを付加できます  
	You can add a watermark to the image with text
- 画像の回転、ミラー反転ができます(1.0.1)  
	Images can be rotated and mirrored  

## 依存関係 Requirement

- Python 3.8.5  
- Pillow 8.3.0  

## 使い方 Usage

```dosbatch
image_resize_sig.exe
```
またはimage_resize_sig.exeのアイコンに変換したいファイルをドラッグ＆ドロップします

- 操作 Operation  
	- 設定ファイル(settings_img_conv.py)の編集  
		Edit configuration file(settings_img_conv.py)  
		- 画像の幅、高さ、上書き指定、Exif情報の扱い、透かし文字列、フォントファイル名、フォントサイズ、文字色、縁取りの色、縁取りの幅、右下からの隙間を指定  
			Specify image width, height, overwrite specification, Exif information handling, watermark character string, font file name, font size, text color, border color, border width, gap from the lower right  
	- アプリの起動  
		Launch the app  
	- 画像の選択  
		Select an image  
		- ファイル選択ダイアログで画像を選択  
			Select an image in the file selection dialog  
		- 起動時に画像をドラッグアンドドロップして画像を選択  
			Select an image by dragging and dropping the image at startup  

## インストール方法 Installation

- pip install pillow  

## プログラムの説明サイト Program description site

[画像サイズを変更し文字透かしを入れるアプリの作り方【Python】 - プログラムでおかえしできるかな](https://juu7g.hatenablog.com/entry/Python/image/resize-sig)  

## 作者 Authors
juu7g

## ライセンス License
このソフトウェアは、MITライセンスのもとで公開されています。LICENSE.txtを確認してください。  
This software is released under the MIT License, see LICENSE.txt.

