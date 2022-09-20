"""
文字透かし付き画像サイズ変更ツール
"""
from PIL import Image, ImageDraw, ImageFont, ImageOps
from tkinter import filedialog
import tkinter as tk
import os, sys, pathlib
sys.path.append(os.path.dirname(sys.executable))    # exeから読めるようにパスに追加
import settings_img_conv

class ImageConversion:
    """
    画像変換クラス
    """
    def scale_to_width(self, img, width):
        """
        アスペクト比を固定して、指定した幅になるようリサイズする。
        Args:
            Int:        幅
        Returns:
            Image:      変換した画像
        """
        height = round(img.height * width / img.width)
        return img.resize((width, height))

    def scale_to_height(self, img, height):
        """
        アスペクト比を固定して、指定した高さになるようリサイズする。
        Args:
            Int:        高さ
        Returns:
            Image:      変換した画像
        """
        width = round(img.width * height / img.height)
        return img.resize((width, height))

    def get_image(self, file_path):
        """
        画像を読み込む
        Args:
            Int:        画像のパス
        Returns:
            Image:      ロードした画像
        """
        try:
            img = Image.open(file_path)
        except:
            print(f"【エラー】サポートしている画像ファイルではありません({file_path})")
            img = None
        return img

    def save_image(self, img:Image, file_path:str, suffix:str, dst_path:str, overwrite:bool=True, **save_kwargs) -> str:
        """
        画像の保存
        Args:
            Image:      保存する画像
            str:        元画像のパス
            str:        サフィックス
            str:        保存先フォルダのパス
            bool:       上書きフラグ
            **:         キーワードオプション
        Returns:
            str:        保存した画像のパス
        """
        # 元のファイル名を拡張子とそれ以外に分ける
        basename = os.path.splitext(os.path.basename(file_path))
        # 保存ファイル名の作成 元のファイル名にsuffixを付加
        new_path = dst_path + "\\" + basename[0] + suffix + basename[1]
        # 別名保存の場合、ファイル名を変える
        if not overwrite:
            x = 1
            while pathlib.Path(new_path).exists():
                new_path = dst_path + "\\" + basename[0] + suffix + "_" + str(x) + basename[1]
                x += 1

        # 保存 JPEGはquality=95で保存。qualityはPNGでは関係ない属性だが、したままでも無視してくれる
        # img.save(new_path, quality=95, **save_kwargs)
        img.save(new_path, quality=100, subsampling=0, **save_kwargs)
        return new_path

    def make_dir(self, target_path:str, base_path:str) -> str:
        """
        フォルダの作成(指定フォルダが存在しない場合に作成する)
        指定されたフォルダ名が相対パスか絶対パスか判断して処理する
        Args:
            str:        指定されたフォルダ
            str:        基準にするフォルダ
        Returns:
            str:        作成したフォルダのパス
        """
        p = pathlib.Path(target_path)
        if not os.path.isabs(p):    # is_absolute()は\\で始まるパスは相対と判断するのでしないisabs()を使用
            p = pathlib.Path(base_path + "\\" + target_path)
        if not p.exists():
            p.mkdir()
        return str(p)

    def set_watermark_by_str(self, img:Image, water_mark:str, size:int
                            , font_name:str, padx:int, pady:int, kwarges) -> str:
        """
        透かしを文字で入れる
        Args:
            Image:      画像
            str:        透かし文字列
            int:        フォントサイズ
            str:        フォントファイル名
            int:        画像の右下からの移動距離(水平方向)
            int:        画像の右下からの移動距離(垂直方向)
            dict:       キーワードオプション
        Returns:
            str:        エラーメッセージ
        """
        err_msg = ""
        sig = water_mark
        draw_img = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype(font_name, size) # フォント名とサイズ(px)
        except:
            err_msg = f"【エラー】フォントファイル名を確認してください({font_name})"
            print(err_msg)
            return err_msg
            # sys.exit()

        # 透かし文字列の大きさを取得し、文字の出力位置を求める
        sig_size = font.getsize(sig)
        sig_nw = (img.size[0] - sig_size[0] - padx, img.size[1] - sig_size[1] - pady)
        try:
            draw_img.text(sig_nw, sig, font=font, **kwarges)
        except:
            # フォントによってはエラーが出る
            err_msg = "【エラー】透かしが書けませんでした。フォント、色を変更してみてください。"
            print(err_msg)

        return err_msg

class ImageUI:
    """
    画像変換クラスを使用して画像変換する操作クラス
    """
    def convert_image_from_dialog_or_args(self, book:dict, paths:list=None) -> set:
        """
        画像変換(リサイズ、回転、反転、Exif除去、透かし)
        コマンドライ引数かファイルダイアログから画像を指定して画像の変更を行い保存する。
        指定により文字透かしを描画する
        Args:
            dict:   設定項目
            list:   画像のパスのリスト
        Returns:
            set:    変換後の画像のパスのセット
            str:    エラーメッセージ
        """
        output_paths = set()    # 出力したファイルパスの集合、戻り値とする
        err_msg = ""

        # コマンドライン引数からドラッグ＆ドロップされたファイル情報を取得
        if paths:
            file_paths = paths
        elif len(sys.argv) > 1:
            file_paths = tuple(sys.argv[1:])
        else:
            # 画像を指定
            root = tk.Tk()      # 自動で作成されるToplevelオブジェクトを手動で作成し
            root.withdraw()     # 撤去状態にする
            file_paths = filedialog.askopenfilenames(
                filetypes=[("画像", ".png .jpg .gif .webp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("GIF", ".gif"), ("WebP", ".webp"), ("すべて", "*")])

        if len(file_paths) == 0:
            err_msg = f"【エラー】対象のファイルがありません"
            print(err_msg)
            return output_paths, err_msg
            # sys.exit()

        dst_img = None
        save_kwarg = {}
        img_conv = ImageConversion()    # インスタンス作成
        # 保存先がなかったら作成
        dst_path = img_conv.make_dir(book.get("dest_path"), os.path.dirname(file_paths[0]))
        print(f"\n◆保存先「{dst_path}」に")

        for file_name in file_paths:
            # 画像の読み込み
            img = img_conv.get_image(file_name)
            if not img: continue    # Imageオブジェクトが作られていなかったらスキップ

            # Exif情報を書き込む場合、読んだ画像のExif情報を保存時に設定
            if book.get("exif"):
                save_kwarg["exif"] = img.getexif()
            else:
                save_kwarg["exif"] = bytes(b"") 
                # JPEGはオプションなしかこの指定でないとExif無しにできない
                # PNGはオプションなしだとExifを出力するのでNoneかこの指定。
            
            # はじめに画像を出力用にコピーしておく
            dst_img = img.copy()

            # 回転      回転は最初に実施、サイズ変更は回転されたものに施すイメージで指定されるから
            if book.get("rotate90"):    # 左回転
                dst_img = dst_img.rotate(90, expand=True)
            if book.get("rotate270"):   # 右回転
                dst_img = dst_img.rotate(270, expand=True)

            # リサイズの幅が指定されていたらその幅に、高さが指定されていたらその高さに
            if not book.get("do_resize", True):   # リサイズしない場合はコピー、追加した設定値なので存在しない場合はTrue
                name_suffix = "_c" 
            elif book.get("width") != 0:
                dst_img = img_conv.scale_to_width(dst_img, book.get("width"))
                name_suffix = f"_w{book.get('width')}" 
            elif book.get("height") != 0:
                dst_img = img_conv.scale_to_height(dst_img, book.get("height"))
                name_suffix = f"_h{book.get('height')}" 
            
            # ミラー反転
            if book.get("mirror"):
                dst_img = ImageOps.mirror(dst_img)

            # 透かし
            if book.get("is_water_mark"):
                kwargs = {"fill":book.get("wm_f_color"),
                            "stroke_width":book.get("wm_stroke"),
                            "stroke_fill":book.get("wm_b_color")}
                wm_err = img_conv.set_watermark_by_str(dst_img, book.get("water_mark"),
                                                book.get("wm_size"),
                                                book.get("wm_font_name"),
                                                book.get("wm_padx"),
                                                book.get("wm_pady"), kwargs)
                if wm_err:
                    err_msg = wm_err

            # 画像を保存    
            if dst_img:
                new_path = img_conv.save_image(
                    dst_img, file_name, name_suffix, dst_path, overwrite=book.get("overwrite"), **save_kwarg)
                print(f"「{os.path.basename(new_path)}」を保存。サイズ {img.size} ⇒ {dst_img.size}")
            
            # 出力したファイルパスを保存
            output_paths.add(new_path)

        return output_paths, err_msg

def get_book_variable_module_name(module_name:str) -> dict:
    """
    モジュールから変数定義を取得し辞書で返す
        Args:
            str:    モジュール名
        Returns:
            dict:   変数定義の辞書
    """
    module = globals().get(module_name, None)
    book = {}
    if module:
        book = {key: value for key, value in module.__dict__.items() if not (key.startswith('__') or key.startswith('_'))}
    return book

if __name__ == "__main__":
    print(f"画像の幅:{settings_img_conv.width}, 高さ:{settings_img_conv.height}, 保存先:{settings_img_conv.dest_path}")
    print(f"上書き:{settings_img_conv.overwrite}, Exif出力:{settings_img_conv.exif}")
    print(f"透かし文字:{settings_img_conv.water_mark}")
    if settings_img_conv.water_mark:
        print(f"　文字色:{settings_img_conv.wm_f_color}, 縁取り色:{settings_img_conv.wm_b_color}, 縁取りの幅:{settings_img_conv.wm_stroke}, 右下の隙間({settings_img_conv.wm_padx}, {settings_img_conv.wm_pady})")
        print(f"　フォント{settings_img_conv.wm_font_name}, サイズ:{settings_img_conv.wm_size}")
    yes_or_no = input("\n上の設定値で実行しますか？(y/n)")
    if yes_or_no != "y":
        print("setting_img_conv.pyファイルを修正保存してから実行してください")
        input("\n確認したらEnterキーを押してください")
        sys.exit()

    book = get_book_variable_module_name("settings_img_conv")
    # tomlにis_water_markを追加したことに合わせた対応 water_markに何か設定されていたらtrueとする
    is_water_mark = bool(book.get("water_mark"))
    book["is_water_mark"] = is_water_mark

    ImageUI().convert_image_from_dialog_or_args(book)
    input("\n確認したらEnterキーを押してください")
