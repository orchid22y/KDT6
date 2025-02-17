/*	*************************************************************************************************
 * 	배열(Array) 선언 및 활용
 * 	: 동일한 데이터 타입의 데이터를 연속된 메모리 공간에 저장하는 것
 *	*************************************************************************************************/
public class EX_Array01 {

	public static void main(String[] args) {
		// 일반 변수와 배열 저장 변수
		// 10과목 점수 저장
		int kor, math, eng, sci, dance; 
		int art, music, com, visual, soci ;
		
		
		// 1개 변수명으로 10과목 점수를 저장 => 배열(Array)
		//배열 선언
		int[] jumsu1;	
		int	  jumsu2[]; 	// 대괄호를 타입명 뒤 또는 변수명 뒤에 작성.
		
		// 배열 선언과 초기화 한번에 하는 법
		int jumsu3[] = new int[] {5,7,9};
		
		
		// 배열 생성 및 저장 즉, 메모리 힙 영역의 주소를 저장함.
		// 배열 변수명은 배열의 메모리 시작 주소를 저장
		jumsu1 = new int[5];
		jumsu2 = new int[3];
		
		// 출력하기									// 한쪽이 String이면 '+'시 연결됨
		System.out.println("jumsu1 : " + jumsu1); 	// >출력>> EX_Array01.java
		System.out.println("jumsu2 : " + jumsu2);	// >출력>> jumsu2 : [I@38af3868
		
		
		
	}

}
