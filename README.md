# OpenCV_Python_Tutorials

目次
- [フィルタの種類](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E3%81%AE%E7%A8%AE%E9%A1%9E)
  - [平均化フィルタ](https://github.com/HBEngineer2021/OpenCV_Python_Tutorials#平均化フィルタ)

## フィルタの種類

- 平均化フィルタ
  
  ```
  # OpenCV関数
  cv2.blur(img, ksize)
  ```
  
  ```
  # OpenCV関数 + numpy
  ddepth = -1
    
  # カーネルサイズ【3 × 3】の場合
  kernel = np.array([[1/9,1/9,1/9],
                       [1/9,1/9,1/9],
                       [1/9,1/9,1/9]])
    
  dst = cv2.filter2D(img, ddepth, kernel)
  ```
  
  <details><summary>サンプルコード</summary>
  
  ```py
  imageName = input("画像名を入力するしてください。\n")
  
  img = cv2.imread("./img/" + imageName)
  
  a = int(input("カーネルサイズaを入力。\n"))
  b = int(input("カーネルサイズbを入力。\n"))
  ksize = (a, b)

  dst = cv2.blur(img, ksize)
  
  outputImage = input("画像名を入力するしてください。\n")
  
  cv2.imwrite("./img/" + outputImage, dst)
  ```
  </details>

- 重み付き平均化フィルタ（加重平均フィルタ）


- ガウシアンフィルタ


- 微分フィルタ


- ソーベルフィルタ


- プリューウィットフィルタ


- ロバーツフィルタ


- 2次微分フィルタ


- ラプラシアンフィルタ


- ゼロ交差


- LoGフィルタ


- アンシャープマスキング


- 鮮鋭化フィルタ


- k最近隣平均化フィルタ


- バイラテラルフィルタ


- ノンローカルミーンフィルタ


- メディアンフィルタ


- モザイク処理


- ローパスフィルタ


- ハイパスフィルタ


- バンドパスフィルタ


- バンドエリミネーションフィルタ


- 高域強調フィルタ


- ウィーナフィルタ


- 逆フィルタ


- ジョイントバイラテラルフィルタ


- ガイデットフィルタ


- ガボールフィルタ


- ベイジアンフィルタ


- カルマンフィルタ


- パーティクルフィルタ


- ブーストラップフィルタ


## リンク
- [OpenCVを使った画像処理](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html#py-table-of-content-imgproc)

- [Python/OpenCV】空間フィルタリングで平滑化・輪郭検出](https://algorithm.joho.info/programming/python/opencv-spatial-filter/)
