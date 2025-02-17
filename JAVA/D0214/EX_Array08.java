/*	************************************************************************************
 *  배열(Array) 선언 및 활용
 *  	2차원 배열	=> 행과 열로 구성
 *  			=> 타입명[][] 변수명;  or 타입명 변수명[][];
 *  	2차원 배열 원소
 *	************************************************************************************/

public class EX_Array08 {

	public static void main(String[] args) {
		// - 2차원 배열 객체 생성 및 초기화
		// - 2행 3열 2차원 배열, 모두 정수
		String[][] nameArray = new String[][] {{"홍", "박","이"},{"Hong","park","Lee"}};
		
		//원소 출력
		for(int row=0; row<nameArray.length; row++)
		{
			for(int col=0; col<nameArray[row].length; col++)
				{
					System.out.println(nameArray[row][col]);
				}
		}

	}

}
 