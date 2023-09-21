public class GCG {
    void main(){
        double nan = Double.NaN;
        double result;
        result = Math.pow(2, nan);
        System.out.println(result);
       
        result = Math.pow(1254, 0);
        System.out.println(result);
       
        result = Math.pow(5, 1);
        System.out.println(result);    }
}
