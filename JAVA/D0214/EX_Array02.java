/*	*************************************************************************************************
 * 	배열(Array) 선언 및 활용
 * 	: 동일한 데이터 타입의 데이터를 연속된 메모리 공간에 저장하는 것
 *	*************************************************************************************************/
public class EX_Array02 {

	public static void main(String[] args) {

		// 배열 선언과 동시에 초기화
		int jumsu3[] = new int[] {5,7,9};
		int jumsu4[] = {10, 20, 30, 40};
		//int jumsu5[5,6,7,8]				//ERROR
		
		// 출력 - 원소 출력 : 배열변수명[인덱스]					
		//					인덱스 : 0 ~ (음수X, 왼쪽에서 오른쪽 순서, 원소 갯수 만큼만 가능)
		System.out.println("jumsu3[0] : " + jumsu3[0]);		// jumsu3[0] : 5
		System.out.println("jumsu3[1] : " + jumsu3[1]);		//jumsu3[1] : 7
		//System.out.println("jumsu3[2] : " + jumsu3[-1]);	// ERROR : 자바에는 -1 인덱스는 없음

		System.out.println();
		
		// - 원소값 변경
		jumsu3[0]=100;
		System.out.println("jumsu3[0] : "+ jumsu3[0]);		// jumsu3[0] : 100
		
		
		//jumsu3[0] = 98.;								//ERROR : 타입 에러
		jumsu3[0] = (int)98.;							// 타입 변환 후 입력 가능
		System.out.println("jumsu3[0] : "+ jumsu3[0]);	// jumsu3[0] : 98
		
	}

}
