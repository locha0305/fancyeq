# fancyeq
## 파이썬 3.x를 위한 식 출력 라이브러리

### 1. 서론


### 2. 의존성 라이브러리
- `pygame 1.9.x`(`2.0.x`부터는 호환성의 문제가 있을수 있습니다)

### 3. 예시
        -b ± √(b^2 - 4ac)
    x = ─────────────────
               2a
  
`fancyeq`는 위와 같은 수식을 아래와 같이 표현하도록 도와줍니다

    x = fancyeq.equation(over(("-b", fancyeq.operation.plus_minus(), fancyeq.operation.sqrt("b", fancyeq.script.superscript("2") , " - 4ac")), "2a")
    
### 4. 패치노트
[]값 출력
[]superscript, subscript
[]over
[]integral, d/dx
[]sqrt
[]sigma, pi
[]else
 
