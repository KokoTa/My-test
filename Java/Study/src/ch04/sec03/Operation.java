package ch04.sec03;

public enum Operation {
    ADD("+") {
        public int eval(int arg1, int arg2) { return arg1 + arg2; }
    },
    SUBTRACT("-") {
        public int eval(int arg1, int arg2) { return arg1 - arg2; }
    },
    MULTIPLY("*") {
        public int eval(int arg1, int arg2) { return arg1 * arg2; }
    },
    DIVIDE("/") {
        public int eval(int arg1, int arg2) { return arg1 / arg2; }
    };

    private String symbol;
    // 这里String symbol指代当前枚举到的对象括号里的值
    Operation(String symbol) { this.symbol = symbol; }
    public String getSymbol() { return symbol; }
    
    public abstract int eval(int arg1, int arg2);
}