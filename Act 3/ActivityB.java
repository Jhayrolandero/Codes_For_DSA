public class ActivityB {

    public int factorial(int n){
        if(n == 1) return 1;
        return(n * factorial(n - 1));
    }

    public int make_ceil(double x) {
        return (int) Math.ceil(x);
    }

    public int make_floor(double x) {
        return (int) Math.floor(x);
    }

    public int get_modulus(int a, int b) {
        return a % b;
    }

    public double get_factorial(int a, int b, int c) {
        return factorial(a) / (factorial(b) * factorial(c));
    }

    public double raised_to_the_power(int a, int b, int c) {
        double exponent = Math.pow(b, c);
        if (b < 0)
            exponent = -exponent;
        if (a < 0)
            return -Math.pow(a, exponent);

        return  Math.pow(a, exponent);
    }

    public double get_log(int num, int base) {
        return (Math.log(num)) / (Math.log(base));
    }

    public int summation(int start, int end){
        int sum = 0;

        for(int i = start; i <= end; i++){
            sum += 2 + i;
        }

        return sum;
    }

    public int summation(int start1, int end1, int start2, int end2) {
        int sum = 0;

        for (int i = start1; i <= end1; i++) {
            for (int j = start2; j <= end2; j++) {
                sum += Math.pow(i, j);
            }
        }

        return sum;
    }

    public static int mix_fraction(int whole, int denominator, int numerator) {
        return whole * denominator + numerator;
    }


    public static void main(String[] args) {
        ActivityB test = new ActivityB();
        System.out.println("Problem 1: " + test.make_floor(3.99));
        System.out.println("Problem 2: " + test.make_floor(-4.5));
        System.out.println("Problem 3: " + test.make_floor(Math.cbrt(30)));
        System.out.println("Problem 4: " + test.make_ceil(6.55));
        System.out.println("Problem 5: " + test.make_ceil(-99.99));
        System.out.println("Problem 6: " + test.make_ceil(mix_fraction(2, 4, 3)));
        System.out.println("Problem 7: " + test.get_modulus(2345, 6));
        System.out.println("Problem 8: " + test.get_modulus(143, 44));
        System.out.println("Problem 9: " + test.get_factorial(5, 3,2));
        System.out.println("Problem 10: " + test.raised_to_the_power(2, 2,3));
        System.out.println("Problem 11: " + test.raised_to_the_power(-3, -2,2));
        System.out.println("Problem 12: " + test.get_log(1024, 2));
        System.out.println("Problem 13: " + test.get_log(250, 5));
        System.out.println("Problem 14: " + test.summation(2, 5));
        System.out.println("Problem 15: " + test.summation(1, 3, 0, 4));
    }
}
