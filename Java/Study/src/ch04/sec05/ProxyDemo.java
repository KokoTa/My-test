package ch04.sec05;


import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.util.Arrays;

// 代理是用于接口的，因为接口不能实例化
public class ProxyDemo {
    public static void main(String[] args) {
        Object[] values = new Object[1000]; // 创建对象数组

        for (int i = 0; i < values.length; i++) {
            Object value = new Integer(i); // 设置的是Interger类的代理
            // 当有方法调用并用到Integer类型的value时，会触发代理的处理器
            values[i] = Proxy.newProxyInstance( // 参数： 类加载器(默认为null)， 接口， 处理器
                null, value.getClass().getInterfaces(),
                (Object proxy, Method m, Object[] margs) -> { // 这里的参数是固定的
                    System.out.println(value + "." + m.getName() + Arrays.toString(margs)); // 打印跟踪信息
                    return m.invoke(value, margs);
                });
        }
        
        int position = Arrays.binarySearch(values, new Integer(200)); // 调用了binarySearch方法，会触发代理处理器
        System.out.println(values[position]);
    }
}
