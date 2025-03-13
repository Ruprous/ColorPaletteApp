# カラーパレットアプリ (Python Tkinter)

import tkinter as tk
from tkinter import colorchooser, Toplevel
from tkinter import ttk
import colorsys
from PIL import ImageGrab  # Pillow (PIL) を利用
import pyautogui  # カーソル位置の取得に使用  # Pillow (PIL) を利用

class ColorPaletteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("カラーパレットアプリ")
        self.root.geometry("900x600")  # ウィンドウサイズを900x600に設定
        self.root.resizable(False, False)  # サイズ変更を禁止
        self.selected_color = "#FFFFFF"
        self.hue = 0
        self.saturation = 0
        self.brightness = 1

        # 色の表示エリア
        self.color_display = tk.Label(self.root, text=self.selected_color, bg=self.selected_color, font=("Arial", 16), width=20, height=2)
        self.color_display.grid(row=0, column=0, columnspan=3, pady=10)

                # スポイトボタン
        spoit_btn = tk.Button(self.root, text="スポイトで色を取得", command=self.start_spoit)
        spoit_btn.grid(row=1, column=1, pady=5)
        choose_color_btn = tk.Button(self.root, text="色を選択", command=self.choose_color)
        choose_color_btn.grid(row=1, column=0, pady=5)

        # 色相スライダー
        self.hue_slider = tk.Scale(self.root, from_=0, to=360, orient="horizontal", label="色相", command=self.update_from_hsv)
        self.hue_slider.grid(row=2, column=0, columnspan=3, pady=5, sticky="ew")

        # 彩度スライダー
        self.sat_slider = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient="horizontal", label="彩度", command=self.update_from_hsv)
        self.sat_slider.grid(row=3, column=0, columnspan=3, pady=5, sticky="ew")

        # 明度スライダー
        self.bright_slider = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient="horizontal", label="明度", command=self.update_from_hsv)
        self.bright_slider.set(1)  # 初期値を1（明るい状態）に設定
        self.bright_slider.grid(row=4, column=0, columnspan=3, pady=5, sticky="ew")

    # 色選択機能
    def choose_color(self):
        color_code = colorchooser.askcolor(title="色を選択")[1]
        if color_code:
            self.selected_color = color_code
            self.color_display.config(text=self.selected_color, bg=self.selected_color)
            self.update_sliders_from_color(self.selected_color)

                            # スポイト機能の開始
    def start_spoit(self):
        # ウィンドウを一時的に隠す
        self.root.withdraw()
        self.root.after(300, self.capture_screen)  # 少し待ってからスクリーンキャプチャ

    # スクリーンショットを取得して色を取得
    def capture_screen(self):
        x, y = pyautogui.position()  # カーソルの位置を取得
        screenshot = ImageGrab.grab()  # スクリーンショットを取得（全モニター対応）
        rgb = screenshot.getpixel((x, y))
        color_code = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        self.selected_color = color_code
        self.color_display.config(text=self.selected_color, bg=self.selected_color)
        self.update_sliders_from_color(self.selected_color)  # スライダーに反映
        self.root.deiconify()  # ウィンドウを再表示
    
        # ウィンドウを一時的に隠す
        self.root.withdraw()
        self.root.after(300, self.capture_screen)  # 少し待ってからスクリーンキャプチャ

    # スクリーンショットを取得して色を取得
    
        x, y = pyautogui.position()  # カーソルの位置を取得
        screenshot = ImageGrab.grab()  # スクリーンショットを取得（全モニター対応）
        rgb = screenshot.getpixel((x, y))
        color_code = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        self.selected_color = color_code
        self.color_display.config(text=self.selected_color, bg=self.selected_color)
        self.update_sliders_from_color(self.selected_color)  # スライダーに反映
        self.root.deiconify()  # ウィンドウを再表示
    
        # ウィンドウを一時的に隠す
        self.root.withdraw()
        self.root.after(300, self.capture_screen)  # 少し待ってからスクリーンキャプチャ

    # スクリーンショットを取得して色を取得
    
        x, y = pyautogui.position()  # カーソルの位置を取得
        screenshot = ImageGrab.grab()  # スクリーンショットを取得（全モニター対応）
        rgb = screenshot.getpixel((x, y))
        color_code = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        self.selected_color = color_code
        self.color_display.config(text=self.selected_color, bg=self.selected_color)
        self.update_sliders_from_color(self.selected_color)  # スライダーに反映
        self.root.deiconify()  # ウィンドウを再表示
    
        # 透明なオーバーレイウィンドウを作成
        self.overlay = Toplevel(self.root)
        self.overlay.attributes("-fullscreen", True)  # フルスクリーン
        self.overlay.attributes("-alpha", 0.01)  # ほぼ透明にする
        self.overlay.attributes("-topmost", True)  # 最前面に表示
        self.overlay.bind("<Button-1>", self.capture_screen)  # 左クリックで色を取得

    # スクリーンショットを取得して色を取得
    
        x, y = self.overlay.winfo_pointerxy()  # カーソルの位置を取得
        screenshot = ImageGrab.grab()  # スクリーンショットを取得
        rgb = screenshot.getpixel((x, y))
        color_code = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        self.selected_color = color_code
        self.color_display.config(text=self.selected_color, bg=self.selected_color)
        self.update_sliders_from_color(self.selected_color)  # スライダーに反映
        self.overlay.destroy()  # オーバーレイを削除して元の画面に戻る
    
        # 透明なオーバーレイウィンドウを作成
        self.overlay = Toplevel(self.root)
        self.overlay.attributes("-fullscreen", True)  # フルスクリーン
        self.overlay.attributes("-alpha", 0.01)  # ほぼ透明にする
        self.overlay.attributes("-topmost", True)  # 最前面に表示
        self.overlay.bind("<Button-1>", self.capture_screen)  # 左クリックで色を取得

    # スクリーンショットを取得して色を取得
    
        x, y = self.overlay.winfo_pointerxy()  # カーソルの位置を取得
        screenshot = ImageGrab.grab()  # スクリーンショットを取得
        rgb = screenshot.getpixel((x, y))
        color_code = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        self.selected_color = color_code
        self.color_display.config(text=self.selected_color, bg=self.selected_color)
        self.update_sliders_from_color(self.selected_color)  # スライダーに反映
        self.overlay.destroy()  # オーバーレイを削除して元の画面に戻る
      # ウィンドウを一時的に隠す
        self.root.after(500, self.capture_screen)  # 少し待ってからスクリーンキャプチャ

    # スクリーンショットを取得して色を取得
      # スクリーンショットを取得
        x, y = self.root.winfo_pointerxy()  # カーソルの位置を取得
        rgb = screenshot.getpixel((x, y))
        color_code = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        self.selected_color = color_code
        self.color_display.config(text=self.selected_color, bg=self.selected_color)
        self.update_sliders_from_color(self.selected_color)  # スライダーに反映
        self.root.deiconify()  # ウィンドウを再表示
    def update_from_hsv(self, event=None):
        self.hue = self.hue_slider.get()
        self.saturation = self.sat_slider.get()
        self.brightness = self.bright_slider.get()
        r, g, b = colorsys.hsv_to_rgb(self.hue/360, self.saturation, self.brightness)
        self.selected_color = f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
        self.color_display.config(text=self.selected_color, bg=self.selected_color)

    # RGB から HSV スライダーを更新
    def update_sliders_from_color(self, color_code):
        color_code = color_code.lstrip('#')
        r, g, b = int(color_code[0:2], 16), int(color_code[2:4], 16), int(color_code[4:6], 16)
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        self.hue_slider.set(h * 360)
        self.sat_slider.set(s)
        self.bright_slider.set(v)

            # カラーパレット管理
        self.palette = []
                # スクロール可能なカラーパレットエリア
                # スクロール可能なカラーパレットエリア
        self.palette_canvas = tk.Canvas(self.root, width=800, height=200)
        self.palette_canvas.grid(row=5, column=0, columnspan=3, pady=10, sticky="nsew")

        self.palette_scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.palette_canvas.yview)
        self.palette_scrollbar.grid(row=5, column=3, sticky="ns")

        self.palette_frame = tk.Frame(self.palette_canvas)
        self.palette_canvas.create_window((0, 0), window=self.palette_frame, anchor="nw")
        self.palette_canvas.config(yscrollcommand=self.palette_scrollbar.set)
        self.palette_canvas.grid(row=5, column=0, columnspan=3, pady=10, sticky="ew")

        self.palette_frame = tk.Frame(self.palette_canvas)
        self.palette_canvas.create_window((0, 0), window=self.palette_frame, anchor="nw")

        self.palette_scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.palette_canvas.yview)
        self.palette_scrollbar.grid(row=5, column=3, sticky="ns")
        self.palette_canvas.config(yscrollcommand=self.palette_scrollbar.set)
        self.palette_frame.grid(row=5, column=0, columnspan=3, pady=10, sticky="ew")

        add_palette_btn = tk.Button(self.root, text="パレットに追加", command=self.add_to_palette)
        add_palette_btn.grid(row=6, column=0, pady=5)

        sort_palette_btn = tk.Button(self.root, text="明度順＋色相順に並び替え", command=self.sort_palette_by_brightness_hue)
        sort_palette_btn.grid(row=6, column=1, pady=5)
        self.palette = []
        self.palette_frame = tk.Frame(self.root)
        self.palette_frame.grid(row=5, column=0, columnspan=3, pady=10, sticky="ew")
        self.palette_listbox.grid(row=5, column=0, columnspan=3, pady=10, sticky="ew")

        add_palette_btn = tk.Button(self.root, text="パレットに追加", command=self.add_to_palette)
        add_palette_btn.grid(row=6, column=0, pady=5)

        sort_palette_btn = tk.Button(self.root, text="明度順＋色相順に並び替え", command=self.sort_palette_by_brightness_hue)
        sort_palette_btn.grid(row=6, column=1, pady=5)

    # パレットに追加
    def add_to_palette(self):
        if self.selected_color not in self.palette:
            self.palette.append(self.selected_color)
            self.update_palette_listbox()

    # パレットのリストボックスを更新
    def update_palette_listbox(self):
        # 既存のパレット表示をクリア
        for widget in self.palette_frame.winfo_children():
            widget.destroy()
        # グリッド状に正方形の色ブロックを配置
        columns = 4  # 4列ずつ並べる
        for index, color in enumerate(self.palette):
            row = index // columns
            column = index % columns
            color_label = tk.Label(self.palette_frame, bg=color, width=10, height=5, relief="ridge", bd=1)
            color_label.grid(row=row, column=column, padx=5, pady=5)
        # スクロール領域の更新
        self.palette_frame.update_idletasks()
        self.palette_canvas.config(scrollregion=self.palette_canvas.bbox("all"))
        # 既存のパレット表示をクリア
        for widget in self.palette_frame.winfo_children():
            widget.destroy()
        # グリッド状に正方形の色ブロックを配置
        columns = 4  # 4列ずつ並べる
        for index, color in enumerate(self.palette):
            row = index // columns
            column = index % columns
            color_label = tk.Label(self.palette_frame, bg=color, width=10, height=5, relief="ridge", bd=1)
            color_label.grid(row=row, column=column, padx=5, pady=5)
        # 既存のパレット表示をクリア
        for widget in self.palette_frame.winfo_children():
            widget.destroy()
        # 新しいパレットを表示
        for color in self.palette:
            color_label = tk.Label(self.palette_frame, bg=color, width=20, height=2, relief="ridge", bd=1)
            color_label.pack(fill="x", pady=2)
        self.palette_listbox.delete(0, tk.END)
        for color in self.palette:
            # カラーコードの代わりに色の四角形を表示
            color_label = tk.Label(self.palette_listbox, bg=color, width=20, height=2)
            self.palette_listbox.insert(tk.END, '')  # 空白のアイテムを追加
            self.palette_listbox.itemconfig(tk.END, {'bg': color})
        self.palette_listbox.delete(0, tk.END)
        for color in self.palette:
            self.palette_listbox.insert(tk.END, color)

    # パレットの並び替え（明度順＋色相順）
    def sort_palette_by_brightness_hue(self):
        def get_hue_brightness(color):
            color = color.lstrip('#')
            r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            return (v, h)  # 明度→色相の順

        self.palette.sort(key=get_hue_brightness)
        self.update_palette_listbox();

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPaletteApp(root)
    root.mainloop()
