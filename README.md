# Python-Image-resize-sig


## �T�v Description
�����������t���摜�T�C�Y�ϊ��c�[��  

Python �� pillow ���g�p���ĉ摜�T�C�Y��ύX���A������������������c�[���ł��B  
You can resize the image and add a text watermark to the image by Python pillow.  

## ���� Features

- �A�X�y�N�g��Œ�ŏc�����̃T�C�Y���w�肵�ăT�C�Y�ύX���܂�  
	Resize by specifying the vertical or horizontal size with a fixed aspect ratio
- �摜�� exe �Ƀh���b�O�A���h�h���b�v���邩�t�@�C���_�C�A���O�őI�����܂�  
	Select the image by dragging and dropping it to the exe or select it in the file dialog
- Exif�����c�����������I���ł��܂�  
	You can choose to keep or erase Exif information
- �摜�ɕ����œ�������t���ł��܂�  
	You can add a watermark to the image with text
- �摜�̉�]�A�~���[���]���ł��܂�(1.0.1)  
	Images can be rotated and mirrored  

## �ˑ��֌W Requirement

- Python 3.8.5  
- Pillow 8.3.0  

## �g���� Usage

```dosbatch
image_resize_sig.exe
```
�܂���image_resize_sig.exe�̃A�C�R���ɕϊ��������t�@�C�����h���b�O���h���b�v���܂�

- ���� Operation  
	- �ݒ�t�@�C��(settings_img_conv.py)�̕ҏW  
		Edit configuration file(settings_img_conv.py)  
		- �摜�̕��A�����A�㏑���w��AExif���̈����A������������A�t�H���g�t�@�C�����A�t�H���g�T�C�Y�A�����F�A�����̐F�A�����̕��A�E������̌��Ԃ��w��  
			Specify image width, height, overwrite specification, Exif information handling, watermark character string, font file name, font size, text color, border color, border width, gap from the lower right  
	- �A�v���̋N��  
		Launch the app  
	- �摜�̑I��  
		Select an image  
		- �t�@�C���I���_�C�A���O�ŉ摜��I��  
			Select an image in the file selection dialog  
		- �N�����ɉ摜���h���b�O�A���h�h���b�v���ĉ摜��I��  
			Select an image by dragging and dropping the image at startup  

## �C���X�g�[�����@ Installation

- pip install pillow  

## �v���O�����̐����T�C�g Program description site

[�摜�T�C�Y��ύX������������������A�v���̍����yPython�z - �v���O�����ł��������ł��邩��](https://juu7g.hatenablog.com/entry/Python/image/resize-sig)  

## ��� Authors
juu7g

## ���C�Z���X License
���̃\�t�g�E�F�A�́AMIT���C�Z���X�̂��ƂŌ��J����Ă��܂��BLICENSE.txt���m�F���Ă��������B  
This software is released under the MIT License, see LICENSE.txt.

