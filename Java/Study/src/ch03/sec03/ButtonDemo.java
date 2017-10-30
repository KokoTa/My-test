package ch03.sec03;

import javafx.application.*;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.*;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.scene.text.*;
import javafx.stage.*;

// From the command line, you can run this program as
// java ch03.sec03.ButtonDemo
// even though it has no main method

public class ButtonDemo extends Application {
   public void start(Stage stage) {
      
      Button cancelButton = new Button("Cancel"); // 创建按钮
      cancelButton.setOnAction(new CancelAction()); // 事件回调
      
      Label message = new Label("Hello, JavaFX!"); // 创建信息
      message.setFont(new Font(100)); // 设置字体
      VBox root = new VBox(); // 创建面板
      root.getChildren().addAll(cancelButton, message); // 载入
      Scene scene = new Scene(root); // 创建显示
      stage.setScene(scene);
      stage.show();
   }
}

class CancelAction implements EventHandler<ActionEvent> { // 事件回调接口
    public void handle(ActionEvent event) {
        System.out.println("Oh noes!");
    }
}