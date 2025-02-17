/* *************************************************************************************
 * 연산자 - 산술연산자
 * - 덧  셈 + 
 * - 뺄  셈 -
 * - 나눗셈 /	: 몫 추출
 * - 나머지 % 
 * ************************************************************************************* */


public class EX_07 {

	public static void main(String[] args) {
		// 변수 선언 및 초기화
		int num1 = 13;
		int num2 = 5;
		
		// 산술 연산 결과 출력
		System.out.printf("%d + %d = %d\n", num1, num2, num1+num2);				// 13 + 5 = 18
		System.out.printf("%d - %d = %d\n", num1, num2, num1-num2);				// 13 - 5 = 8
		System.out.printf("%d * %d = %d\n", num1, num2, num1*num2);				// 13 * 5 = 65
		System.out.printf("%d / %d = %d\n", num1, num2, num1/num2);				// 13 / 5 = 2
		System.out.printf("%d %% %d = %d\n", num1, num2, num1%num2);			// 13 % 5 = 3
		
		
		//			int / int => 결과 int 몫만 추출
		//  (double)int / int => 큰 데이터 타입으로 자동 형변환 후 계산 진행
		System.out.printf("%d / %d = %f\n", num1, num2,(float) num1/num2);		// 13 / 5 = 2.600000

	}

}
