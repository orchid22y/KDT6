/*	**********************************************************************************************
 * 	제어문 - coutinue문
 * 			반복 중단하고 다음 반복으로 진행 시킴
 * 			아래쪽 코드 실행되지 않음
 * 			while/do~while에서는 무한 반복에 빠질 위험 있음
 * 			※주의※ coutinue 전에 값의 증감 처리 필수
 *	**********************************************************************************************/
public class EX_Countinue {
	public static void main(String[] args) {
		
		// [ 1 ~ 10 범위에서 2의 배수만 출력 ]
		
		
		// for 문과 coutinue문
		
		//		1		2	3	
		for(int n=1; n<=10; n++)
		{
			if(n%2==1)continue;	// 조건문이 참일 경우 3번 n++로 이동
				System.out.println(n);	// 조건문이 거짓일때 실행
		}
		
		
		// while 문과 continue 문
		int count=0;
		
		//		(1)		
		while(count<=10)
		{	
			count++;
			if(count%2==1) continue;	// (1)로 이동
			System.out.println(count);	//	(count%2==1)이 거짓일 때 실행
			
		}
		
		
		// do ~ while 문과 continue문
		
		int value=0;
		
		do {//(1)
			value++;
			if(count%2==1) continue;	// (2)로 이동
			System.out.println(value);
			
		}while(value<10);	//(2) 
		
		
		
	}

}
