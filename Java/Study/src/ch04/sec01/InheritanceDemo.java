package ch04.sec01;

public class InheritanceDemo {
    public static void main(String[] args) {
        Manager boss = new Manager("Fred", 200000);
        boss.setBonus(10000); // Defined in subclass 调用Manager类自身方法
        System.out.println(boss.getSalary());
        boss.raiseSalary(5); // Inherited from superclass 调用继承方法
        System.out.println(boss.getSalary());        
        Employee empl = boss; // Ok to convert to superclass 子类可以设定为父类的类型
        empl.raiseSalary(5); // Can still apply superclass methods 可以调用这个父类的方法，但是调用不了子类的方法了
        System.out.println(empl.getSalary()); // Calls Manager.getSalary
        
        if (empl instanceof Manager) { // 需要让父类引用转换为子类引用
            Manager mgr = (Manager) empl;
            mgr.setBonus(20000);
        }
    }
}