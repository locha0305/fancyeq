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

```python
x = fancyeq.equation(over(("-b", fancyeq.operation.plus_minus(), fancyeq.operation.sqrt("b", fancyeq.script.superscript("2") , " - 4ac")), "2a")
```

모든 함수는 
```python
def sqrt(tokens):
        if isinstance(tokens, str):
                pass #만약 입력이 문자열 형태 '2a'이면
        else:
                pass #만약 입력이 토큰 형태 '[{"text":"2a", "type":text"}, {"text":"2", "type":subscript"}]'이면
        return tokens #토큰 형태로 반환 '{"text":{"text":"b", "type":"normal"}, {"text":"2", "type":"superscript"}, {"text":"-4ac", "type":"normal"}, "type":"sqrt", "length":length}' 
       
```
`equation` 오브젝트에서 입력을 받을때는 토큰으로 받으며 각각의 토큰을 출력하는 형태로 실행됩니다

#### 4. 토큰
##### i) 타입

    
### 4. 패치노트
- 1차 목표
- [ ] show text
- [ ] subscript, superscript
- [ ] over
- 2차 목표
- [ ] integral, differential
- 3차 목표
- [ ] sqrt
- [ ] sigma, pi



 
