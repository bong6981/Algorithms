package bronzeIV;

import java.util.Scanner;

public class Boj_1330 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();

        int result = x-y;

        if(result==0) {
            System.out.println("==");
        } else if(result<0) {
            System.out.println("<");
        } else {
            System.out.println(">");
        }
    }
}
