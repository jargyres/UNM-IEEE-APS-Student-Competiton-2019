import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.image.BufferedImage;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

public class FinalResults extends JPanel {

    public boolean FinalResultsPanelShowing = false;

    public BufferedImage S11Pic;

    public int S11PicCount = 0;

    public BufferedImage RP2DPic;

    public int RP2DPicCount = 0;

    public BufferedImage RP3DPic;

    public int RP33DPicCount = 0;



    public void runCMD(ProcessBuilder pro){
        try {


            var process = pro.start();

            var reader =
                    new BufferedReader(new InputStreamReader(process.getInputStream()));

            String line;

            while ((line = reader.readLine()) != null) {
                System.out.println(line);

            }


        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    public boolean checkifFileExists(String filestring){
        File temp;
        try{
            ClassLoader classLoader = getClass().getClassLoader();

            temp = new File(classLoader.getResource(filestring).getFile());

            return temp.exists();

        }catch (Exception e){

            return false;

        }

    }

    public FinalResults(){

        setBackground(Color.lightGray);

        setLayout(new GridLayout(1,3));








    }

}
