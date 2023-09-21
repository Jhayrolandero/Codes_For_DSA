public class Summation {
    public int problem1() {
        int sum = 0;
        for (int k = 3; k <= 7; k++) {
            sum += k;
        }
        return sum;
    }

    public int problem2() {

        int sum = 0;
        for (int i = 2; i <= 5; i++) {
            sum += 2 * i;
        }

        return sum;
    }

    public String problem3() {

        String sum = "";
        for (int j = 1; j <= 4; j++) {
            if(j == 4){
                sum += STR."\{j}x";
                continue;
            }
            sum += STR."\{j}x + ";
        }

        return sum;
    }

    public String problem4() {

        String sum = "";
        for (int k = 2; k <= 4; k++) {
            if(k == 4){
                sum += STR."(\{Math.pow(k, 2)} + \{3*k}x + 1)";
                continue;
            }
            sum += STR."(\{Math.pow(k, 2)} + \{3*k}x + 1) + ";
        }

        return sum;
    }

    public String problem5() {

        String sum = "";
        for (int n = 0; n <= 3; n++) {
            if(n == 3){
                sum += STR."(\{n} + x)";
                continue;
            }
            sum += STR."(\{n} + x) + ";
        }

        return sum;
    }

    
    void main() {
        System.out.println(STR."Problem 1: \{problem1()}");
        System.out.println(STR."Problem 2: \{problem2()}");
        System.out.println(STR."Problem 3: \{problem3()}");
        System.out.println(STR."Problem 4: \{problem4()}");
        System.out.println(STR."Problem 5: \{problem5()}");
    }
}
