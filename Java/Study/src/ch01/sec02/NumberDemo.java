package ch01.sec02;

public class NumberDemo {
    public static void main(String[] args) {
        System.out.println(4000000000L); // long literal 长整型
        System.out.println(0xCAFEBABE); // hex literal 16进制
        System.out.println(0b1001); // binary literal 2进制
        System.out.println(011); // octal literal 8进制
        
        // Underscores in literals   助记符
        System.out.println(1_000_000_000); 
        System.out.println(0b1111_0100_0010_0100_0000);
        
        // Advanced topic: Unsigned quantities 无符号位0-255的范围，-127 对应 129， -1 对应 255
        System.out.println(Byte.toUnsignedInt((byte )-127));
        
        System.out.println(3.14F); // float literal
        System.out.println(3.14); // double literal
        System.out.println(3.14D); // double literal
        System.out.println(0x1.0p-3); // hex double literal

        // Infinity and NaN
        System.out.println(1.0 / 0.0); // Infinite
        System.out.println(-1.0 / 0.0); // -Infinite
        System.out.println(0.0 / 0.0); // NaN
        
        System.out.println(1.0 / 0.0 == Double.POSITIVE_INFINITY); // true
        System.out.println(-1.0 / 0.0 == Double.NEGATIVE_INFINITY); // true
        System.out.println(0.0 / 0.0 == Double.NaN); // false

        System.out.println(Double.isInfinite(1.0 / 0.0)); // true
        System.out.println(Double.isNaN(0.0 / 0.0)); // true
        System.out.println(Double.isFinite(0.0 / 0.0)); // false
        
        // Roundoff error
        
        System.out.println(2.0 - 1.1);
        
        // Character literals
        
        System.out.println('J'); 
        System.out.println('J' == 74); 
        System.out.println('\u004A'); 
        System.out.println('\u263A'); 
    }
}