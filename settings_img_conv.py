"""
image_resize-sig.py用設定ファイル
"""
dest_path = r"."				# 保存用フォルダ 相対パス(読んだ画像のフォルダから見て)、絶対パスとも可
width = 600         			# 新しい画像の幅(width)
height = 0          			# 新しい画像の高さ 幅が0の時に有効(height)
overwrite = True    			# 新しい画像のファイル名(_w300などが付加される)
                    			# True:上書き、False:末尾に数字を付加して別名保存
exif = False        			# Exif情報の書き込み True:書き込む、False:書かない

# 透かし用設定(for water mark)
water_mark = ""					# 透かしの指定(""なら入れない)("":No water mark)
wm_font_name = "msgothic.ttc"	# フォントファイル名(font file name)
wm_size = 12					# フォントサイズ(font size)
wm_f_color = "gold"				# 文字色(font coloer)
wm_b_color = "black"			# 縁取りの色(stroke color)
wm_stroke = 0					# 縁取りの幅(px)(stroke width)
wm_padx = 5						# 右下からの隙間(from bottom right)
wm_pady = 5						# 右下からの隙間(from bottom right)