import java.util.Map;
import java.util.HashMap;
public class maps {
    public static void main(String[] args){
        Map cars = new HashMap();
        cars.put("BMW",3);
        cars.put("audi",4);
        cars.put("yamaha",44);
        cars.put("suzuki",7);
        System.out.println(cars);
        cars.remove("BMW");
        int size = cars.size();
        System.out.println(size);
        System.out.println(cars.get("yamaha"));
        System.out.println(cars);
        System.out.println(cars);
    }
}
