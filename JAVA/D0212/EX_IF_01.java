/* ********************************************************************************************
 * 	제어문 - 조건문
 * ********************************************************************************************/


public class EX_IF_01 {

	public static void main(String[] args) {
		// 짝수 홀수 구분
		int num = 11;
		
		// 짝수 홀수 여부 출력
		if (num%2==0) {
			System.out.println("짝수");
		}
		else {
			System.out.println("홀수");
		}

		// 짝수 홀수 여부 출력
		// 결과 출력이 1줄일 경우 '{}' 생략 가능, 들여쓰기 상관 X
		if (num%2==0)
		System.out.println("짝수");

		else
		System.out.println("홀수");
		
		// 삼항 연산자? : 
		String msg = (num%2==0)?"짝수":"홀수"; //조건문이 true면 msg에 짝수를 저장하고, false면 홀수 저장
		System.out.println(msg);
		
		//1줄로 표현하기
		System.out.println((num%2==0) ? "짝수" : "홀수");		
	}
}