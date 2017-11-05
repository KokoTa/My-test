package Calculate;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MyCalculate {
    private JFrame jf; // 框架
    private JPanel jp1, jp2; // 面板
    private JTextField jtf; // 结果显示区文本
    private JButton[] jbs; // 按钮
    private JButton c_jbs; // 重置键
    private String str0 = "0"; // 初始文本
    private String cal = ""; // 输入的计算文本
    private Boolean flag = true; // 小数点标识
    private Boolean overload = false; // 得出结果后，下一次点击重置

    // 引入JS引擎
    private Object res = null; // 计算结果
    private ScriptEngineManager manager = new ScriptEngineManager();
    private ScriptEngine engine = manager.getEngineByName("js");

    public MyCalculate() {
        jf = new JFrame("计算器");
        jp1 = new JPanel();
        jp2 = new JPanel();
        jtf = new JTextField(14); // 显示区14列
        jbs = new JButton[16]; // 16个按钮
        c_jbs= new JButton("C");
        String s = "123+456-789*0.=/";
        for(int i=0; i<jbs.length; i++) { // 按钮内容填充
            jbs[i] = new JButton(s.substring(i, i+1));
        }

        init(); // 布局
        logic(); // 逻辑
    }

    // UI设置
    public void init() {
        // 面板一
        jp1.setLayout(new FlowLayout()); // 横向流布局
        jp1.add(jtf);
        jp1.add(c_jbs);
        jtf.setEditable(false); // 不可编辑
        jtf.setText("0");
        // 面板二
        jp2.setLayout(new GridLayout(4, 4)); // 网格布局
        for(int i=0; i<jbs.length; i++) {
            jp2.add(jbs[i]);
        }
        // 框架布局
        jf.add(jp1, BorderLayout.NORTH);
        jf.add(jp2, BorderLayout.CENTER);
    }

    // UI显示
    public void show() {
        jf.setVisible(true);
        jf.setSize(600, 400);
        jf.setLocation(200, 200);
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // 关闭按钮
        setFontAndColor();
    }

    // 字体和背景色
    public void setFontAndColor() {
        Font f = new Font("微软雅黑", Font.BOLD, 20);
        jtf.setFont(f);
        Color c = new Color(193, 255 ,193);
        c_jbs.setBackground(c);
        jp1.setBackground(Color.lightGray);
        for(int i=0; i<jbs.length; i++) {
            jbs[i].setBackground(Color.WHITE);
        }
    }

    // 逻辑
    public void logic() {
        // 监听重置键
        c_jbs.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String str = e.getActionCommand(); // 获得按键上的内容
                if(str.equals("C")) {
                    str0 = "0";
                    cal = "";
                    flag = true;
                    jtf.setText(str0);
                }
            }
        });
        // 监听数字符号键
        for(int i=0; i<jbs.length; i++){
            jbs[i].addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    String str = e.getActionCommand();

                    if(str.equals("=")) {
                        try {
                            res = engine.eval(cal);
                        } catch(Exception err) {
                            System.out.println(err);
                        }
                        overload = true;
                        jtf.setText(String.valueOf(res));
                    } else if(str.equals(".")) {
                        if(flag.equals(true)) {
                            flag = false;
                            cal += str;
                        }
                        jtf.setText(cal);
                    } else {
                        if(overload.equals(true)) {
                            str0 = "0";
                            cal = "";
                            flag = true;
                            jtf.setText(str0);
                            overload = false;
                        }
                        cal += str;
                        jtf.setText(cal);
                    }
                }
            });
        }
    }
}
