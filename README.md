# fancyeq
## 파이썬 3.x를 위한 식 출력 라이브러리

### 1. 서론


### 2. 의존성 라이브러리
- `pygame 1.9.x ~ 2.0.x`

### 3. 예시
        e^iπ = -1
`fancyeq`는 위와 같은 수식을 아래와 같이 표현하도록 도와줍니다


```python
euler = fancyeq.equation('C:\WINDOWS\FONTS\TIMES', 37, (255, 255, 255), {"text":"e", "type":"default"}, {"text":"iπ", "type":"superscript"}, {"text":"= -1", "type":"default"})
```

`equation` 오브젝트에서 입력을 받을때는 토큰으로 받으며 각각의 토큰을 출력하는 형태로 실행됩니다

```python
from fancyeq import fancyeq
import pygame

screen = pygame.display.set_mode((500, 500))


fancyeq.init()
eq = fancyeq.equation('C:\WINDOWS\FONTS\TIMES', 35, (255, 255, 255), {"text":"p", "type":"default"}, {"text":"ij", "type":"subscript"}, {"text":" = p", "type":"default"}, {"text":"(i - 1)(j - 1)", "type":"subscript"}, {"text":"+ p", "type":"default"}, {"text":"(i - 1)j", "type":"subscript"})
eq.display(screen, (100, 50))
pygame.display.update()
```

#### 4. 토큰
##### i) 타입
1. default
2. superscript

    
### 4. 패치노트
- 1차 목표
- [x] show text
- [x] subscript, superscript
- [ ] over
- 2차 목표
- [ ] integral, differential
- 3차 목표
- [ ] sqrt
- [ ] sigma, pi
- 4차 목표
- [ ] string to text
- [ ] string to equation


 
