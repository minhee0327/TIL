# 08\_Transitions & Transforms

1. transition\(단축\): css 속성의 시작과 끝을 지정\(전환효과\)하여 중간 값을 애니메이션
   * 개별속성
     * transition-property: 전환 효과를 사용할 속성 이름 \(기본값: all\)
       * all: 모든 속성에 적용
       * 속성이름: 전환 효과를 사용할 속성 이름
     * transition-duration: 전환 효과의 지속시간 설정 \(기본값: 0s\)
       * 1s == 1000ms
       * 0.4s == .4s
     * transition-timing-function: [타이밍 함수 지정\(ease\)](https://easings.net/)
       * ease : 빠르게-느리게 \(cubic-bezier\(.25,.1,.25,1\)\)

         -linear: 일정하게 \(cubic-bezier\(0,0,1,1\)\)

       * ease-in: 느리게-빠르게\(cubic-bezier\(0.42,0,1,1\)\)
       * ease-out: 빠르게-느리게 \(cubic-bezier\(0,0,0.58,1\)\)
       * ease-in-out: 느리게-빠르게-느리게 \(cubic-bezier\(0.42,0,.58,1\)\)
       * cubic-bezier\(n,n,n,n\): 자신만의 값 정의\(0~1\)
       * steps\(n\): n번 분할된 에니메이션
     * transition-delay: 전환 효과의 대기시간 설정
       * 시간: 전환 효과의 대기 시간을 설정 \(몇s\)
2. transform
   * 요소의 변환 효과\(변형\)를 지정
   * 사용예시

     ```css
       .box{
           transform: 변환함수1 변환함수2 변환함수3 ...;
           transform: 원근법 이동 크기 회전 기울임
       }
     ```

   * 변환 2D 속성
     * translate\(x, y\): 이동\(x축, y축\) - 단위: 단위
       * translateX\(x\)
       * translateY\(y\)
       * position처럼 배치 후 끝낼 때가 아니라 지속적으로 이동할때 쓰기 좋음
       * position으로 animation을 구성하면 최적화 되지 않은상태 
     * scale\(x,y\): 크기\(x축, y축\) - 단위: 없음\(배수\)
       * scaleX\(x\)
       * scaleY\(y\)
     * rotate\(degree\): 회전\(각도\) - 단위: deg
     * skew\(x-deg, y-deg\): 기울임 - 단위: deg
       * skewX\(x-deg\)
       * skewY\(y-deg\)
     * matrix\(n,n,n,n,n,n\): 2차원 변환 효과
   * 변환 3D 속성
     * translate3d\(x, y,z\): 이동\(x축, y축, z축\) - 단위: 단위
       * translateZ\(z\)
     * scale3d\(x,y,z\): 크기\(x축, y축, z축\) - 단위: 없음\(배수\)
       * scaleZ\(z\)
     * rotate3d\(x, y, z, a\): 회전\(x벡터, y벡터, z벡터, 각도\) - 단위: deg
       * rotateX\(x\)
       * rotateY\(y\)
       * rotateZ\(z\)
     * perspective\(n\): 원근법\(거리\) - 단위
       * 사용시 맨 앞에 선언할 것\(안그러면 적용 안되 보임\)
     * matrix\(n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n\): 3차원 변환 효과
   * 일반 속성
     * trnasform-origin: 요소 변환 기준점을 설정
       * X축: left, right, center, %, 단위 \(기본값: 50%\)
       * Y축: top, bottom, center, %, 단위 \(기본값: 50%\)
       * Z축: 단위 \(기본값: 0\)
     * transform-style: 3D 변환 요소의 자식 요소도 3D 변환을 사용할지 설정
       * flat: 자식요소의 3D 변환을 사용하지 않음\(기본값\)
       * preserve-3d: 자식 요소의 3D 변환을 사용함
     * perspective: 하위 요소를 관찰하는 원근 거리를 설정
       * px, em, cm등 단위로 지정
       * 되도록 **상위요소**에 적용하는게 좋다\(관찰 대상의 부모요소\)
       * 기준점: perspective-origin

         > transform: perspective\(\) 변환함수는  
         > **관찰대상에 직접 적용**하여 그 대상을 관찰하는 원근 거리 설정!  
         > 기준점: transform-origin
     * perspective-origin: 원근 거리의 기준점 설정
       * X축: left, right, center, %, 단위 \(기본값: 50%\)
       * Y축: top, bottom, center, %, 단위 \(기본값: 50%\)
     * backface-visibility: 3D 변환으로 회전된 요소의 뒷면 숨김을 설정
       * visible: 뒷면 숨기지 않음\(기본값\)
       * hidden: 뒷면 숨김
     * matrix\(a,b,c,d,e,f\): 요소의 2차원 변환\(transform\) 효과를 지정
       * scale\(\), skey\(\), translate\(\)그리고 rotate\(\)를 지정

         > 요소에 일반 변환\(transforms\)함수 \(2d, 3d\)를 사용하더라도  
         > 브라우저에 의해 matrix 함수로 계산되어 적용된다.  
         > 2D 변환 함수는 matrix로 3D 변환 함수는 matrix3d로  
         > 따라서 일반적인 경우는 matrix 함수가 아닌 일반변환 함수를 사용하면 됩니다.

