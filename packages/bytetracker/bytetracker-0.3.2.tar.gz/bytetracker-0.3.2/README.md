<div align="center">
<h2>
  ByteTrack-Pip: Packaged version of the ByteTrack repository  
</h2>
<h4>
    <img width="700" alt="teaser" src="assets/demo.gif">
</h4>
<div>
    <a href="https://pepy.tech/project/bytetracker"><img src="https://pepy.tech/badge/bytetracker" alt="downloads"></a>
    <a href="https://badge.fury.io/py/bytetracker"><img src="https://badge.fury.io/py/bytetracker.svg" alt="pypi version"></a>
</div>
</div>

## <div align="center">Overview</div>

This repo is a packaged version of the [ByteTrack](https://github.com/ifzhang/ByteTrack) algorithm.
### Installation
```
pip install bytetracker
```

### Detection Model + ByteTrack 
```python
from bytetracker import BYTETracker

tracker = BYTETracker(args)
for image in images:
   dets = detector(image)
   online_targets = tracker.update(dets)
```
### Reference:
 - [Yolov5-Pip](https://github.com/fcakyon/yolov5-pip)
 - [ByteTrack](https://github.com/ifzhang/ByteTrack)

### Citation
```bibtex
@article{zhang2022bytetrack,
  title={ByteTrack: Multi-Object Tracking by Associating Every Detection Box},
  author={Zhang, Yifu and Sun, Peize and Jiang, Yi and Yu, Dongdong and Weng, Fucheng and Yuan, Zehuan and Luo, Ping and Liu, Wenyu and Wang, Xinggang},
  booktitle={Proceedings of the European Conference on Computer Vision (ECCV)},
  year={2022}
}
```
