package ch04.sec03;

public enum Modifier {
    PUBLIC, PRIVATE, PROTECTED, STATIC, FINAL, ABSTRACT;
    private int mask;
    // private static int maskBit = 1; 不要这样做

    // 不能在构造函数中访问静态变量
    // 但可以在静态初始化块中进行初始化工作
    static {
        int maskBit = 1;
        for (Modifier m : Modifier.values()) {
            m.mask = maskBit;
            maskBit *= 2; 
        }
    }
    
    public int getMask() {
        return mask;
    }
}