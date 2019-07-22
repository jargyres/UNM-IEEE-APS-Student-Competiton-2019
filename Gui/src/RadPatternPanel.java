import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class RadPatternPanel extends JPanel {

    public JTextField rptextfield = new JTextField(20);

    public JTextArea rptextarea = new JTextArea(70,30);

    public PrintStream rpprintstream;

    public String rpsubmittionstring = "Submit frequency";

    public boolean RadPatternpanelShowing = false;


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

    public boolean checkInputforRealNumber(String inputstr){
        boolean result = false;
        try{
            Double x = Double.parseDouble(inputstr);
            if(x <= 3.8 && x >= 0.3){
                result = true;
                rpsubmittionstring = "Submit frequency";
            }
        }catch (NumberFormatException e){

        }

        if(result){
            rpsubmittionstring = "Submit frequency";
        }else{
            rpsubmittionstring = "Invalid frequency";
        }
        return result;

    }

    public boolean checkforRealDistance(String inputstr){

        boolean result = false;
        try{

            Double x = Double.parseDouble(inputstr);
            if(x <= Double.MAX_VALUE && x >= Double.MIN_VALUE){
                result = true;
            }

        }catch(NumberFormatException e){

        }

        return result;

    }



    public RadPatternPanel(){

        setBackground(Color.lightGray);

        setLayout(new GridLayout(1,2));

        JPanel insiderpPanel = new JPanel();

        insiderpPanel.setBackground(Color.lightGray);

        JButton submitfrequency = new JButton(rpsubmittionstring);

        submitfrequency.setEnabled(false);

        JButton run2dRP = new JButton("Run 2D Radiation Pattern");

        JButton run3dRP = new JButton("Run 3D Radiation Pattern");

        run3dRP.setEnabled(false);

        run2dRP.setEnabled(false);

        rptextfield.setText("Enter frequency in GHz");

        rpprintstream = new PrintStream(new CustomOutputStream(rptextarea));

        JScrollPane RPScrollPane = new JScrollPane(rptextarea);


        run2dRP.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                ClassLoader classLoader = getClass().getClassLoader();
                File fi =
                        new File(classLoader.getResource("GeneralizedRadiationPatternMeasurement").getFile());
                runCMD(new ProcessBuilder(fi.toString(), rpsubmittionstring));

                rptextarea.selectAll();
                rptextarea.replaceSelection("Saving Radiation Pattern to " +
                        "Results");

                File fil =
                        new File(classLoader.getResource("save2DRadPattern").getFile());
                runCMD(new ProcessBuilder(fil.toString()));

//                runNewScript.setEnabled(true);

                rptextarea.selectAll();
                rptextarea.replaceSelection("");

            }
        });
        run3dRP.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {




                ClassLoader classLoader = getClass().getClassLoader();
                File fi =
                        new File(classLoader.getResource(
                                "Generalized3DRadPattern").getFile());
                runCMD(new ProcessBuilder(fi.toString(), rpsubmittionstring));

                File fil =
                        new File(classLoader.getResource(
                                "saveMatLab3DImage").getFile());
                runCMD(new ProcessBuilder(fil.toString()));



                rptextarea.selectAll();
                rptextarea.replaceSelection("");

            }
        });

        submitfrequency.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                rpsubmittionstring = rptextfield.getText();
                rpsubmittionstring = rpsubmittionstring + "e9";
                submitfrequency.setText("Frequency set to " + rptextfield.getText() + " GHz");
                submitfrequency.setEnabled(false);
            }
        });

        rptextfield.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                rptextfield.setText("");
                String text = rptextfield.getText();
                if(text.equals("")){
                    submitfrequency.setEnabled(false);
                    run2dRP.setEnabled(false);
                    run3dRP.setEnabled(false);
                }else{
                    submitfrequency.setEnabled(true);
                    run2dRP.setEnabled(true);
                    run3dRP.setEnabled(true);
                }
                submitfrequency.setText(rpsubmittionstring);
            }
        });

        rptextfield.addKeyListener(new KeyAdapter() {
            @Override
            public void keyReleased(KeyEvent e) {
                String text = rptextfield.getText();
                if(text.equals("") || text.equals("Enter frequency in GHz") || !checkInputforRealNumber(text)){
                    submitfrequency.setEnabled(false);
                    run2dRP.setEnabled(false);
                    run3dRP.setEnabled(false);

                }else{
                    submitfrequency.setEnabled(true);
                    run2dRP.setEnabled(true);
                    run3dRP.setEnabled(true);

                }

                submitfrequency.setText(rpsubmittionstring);
            }


        });


        insiderpPanel.add(rptextfield);
        insiderpPanel.add(submitfrequency);
        insiderpPanel.add(run2dRP);
        insiderpPanel.add(run3dRP);

        insiderpPanel.add(RPScrollPane);

        add(insiderpPanel);

    }



}
