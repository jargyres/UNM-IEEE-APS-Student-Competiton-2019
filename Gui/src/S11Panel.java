import javax.swing.*;
import javax.swing.text.DefaultCaret;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.util.ArrayList;


public class S11Panel extends JPanel {

    public String S11submittionstring = "Submit frequency";

    public JTextField s11textField = new JTextField(20);

    public boolean S11PanelShowing = false;

//    public String frequency;

    public String bandwidthString;

    public String resolutionString;

    public JTextArea S11TextArea = new JTextArea(70, 30);

    public PrintStream S11PrintStream;

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
                S11submittionstring = "Submit frequency";
            }
        }catch (NumberFormatException e){

        }

        if(result){
            S11submittionstring = "Submit frequency";
        }else{
            S11submittionstring = "Invalid frequency";
        }
        return result;

    }

    public S11Panel(){

        setBackground(Color.lightGray);
        setLayout(new GridLayout(1,2));

        JPanel insideS11Panel = new JPanel();

        insideS11Panel.setBackground(Color.lightGray);

        s11textField.setText("Enter frequency in GHz");

        JButton calculateBandwidth = new JButton("Calculate Bandwidth");

        calculateBandwidth.setEnabled(false);

        JButton runS11Part1 = new JButton("Run S11 Measurement Part 1");

        runS11Part1.setEnabled(false);

        JButton submitfrequency = new JButton(S11submittionstring);

        submitfrequency.setEnabled(false);

        String[] resolutionStrings = {"Choose Resolution", "High", "Medium",
                "Low"};

        JComboBox resolution = new JComboBox(resolutionStrings);

        resolution.setEnabled(false);

        String[] bandwidthStrings = {"Choose bandwidth", "600 MHz", "400 MHz"
                , "200 MHz"};

        JComboBox bandwidth = new JComboBox(bandwidthStrings);

        bandwidth.setEnabled(false);

        S11PrintStream = new PrintStream(new CustomOutputStream(S11TextArea));

        JScrollPane S11ScrollPane = new JScrollPane(S11TextArea);


        submitfrequency.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                S11submittionstring = s11textField.getText();
                S11submittionstring = S11submittionstring + "e9";
                submitfrequency.setText("Center frequency set to " + s11textField.getText() + " GHz");
                submitfrequency.setEnabled(false);
                resolution.setEnabled(true);
            }
        });


        JButton runS11Part2 = new JButton("Run S11 Measurement Part 2");

        runS11Part2.setEnabled(false);

        runS11Part1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                ClassLoader classLoader = getClass().getClassLoader();
                File fi =
                        new File(classLoader.getResource("GuiS11_Part1").getFile());

                runCMD(new ProcessBuilder(fi.toString(), S11submittionstring,
                 resolutionString, bandwidthString));

                runS11Part2.setEnabled(true);

                runS11Part1.setEnabled(false);
            }
        });

        runS11Part2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                S11TextArea.selectAll();
                S11TextArea.replaceSelection("");
                ClassLoader classLoader = getClass().getClassLoader();
                File fi =
                        new File(classLoader.getResource("GuiS11_Part2").getFile());
                runCMD(new ProcessBuilder(fi.toString(), S11submittionstring,
                        resolutionString, bandwidthString));

                File fil =
                        new File(classLoader.getResource("saveS11Plot").getFile());
                runCMD(new ProcessBuilder(fil.toString()));

                calculateBandwidth.setEnabled(true);

            }
        });



        s11textField.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                s11textField.setText("");
                String text = s11textField.getText();
                if(text.equals("")){
                    submitfrequency.setEnabled(false);
                    runS11Part1.setEnabled(false);
                }else{
                    submitfrequency.setEnabled(true);
//                    runS11Part1.setEnabled(true);
                }
                submitfrequency.setText(S11submittionstring);
            }
        });


        s11textField.addKeyListener(new KeyAdapter() {
            @Override
            public void keyReleased(KeyEvent e) {
                String text = s11textField.getText();
                if(text.equals("") || text.equals("Enter frequency in GHz") || !checkInputforRealNumber(text)){
                    submitfrequency.setEnabled(false);
                    runS11Part1.setEnabled(false);
                }else{
                    submitfrequency.setEnabled(true);
//                    runS11Part1.setEnabled(true);
                }

                submitfrequency.setText(S11submittionstring);
            }

        });



        resolution.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JComboBox cb = (JComboBox)e.getSource();
                String word = (String)cb.getSelectedItem();
                if(word.equals("High")){
//                    S11submittionstring = S11submittionstring + " 1e6";
                    resolutionString = "1e6";
                    bandwidth.setEnabled(true);

                }else if(word.equals("Medium")){
//                    S11submittionstring = S11submittionstring + " 5e6";
                    resolutionString = "5e6";
                    bandwidth.setEnabled(true);

                }else if(word.equals("Low")){
//                    S11submittionstring = S11submittionstring + " 1e7";
                    resolutionString = "1e7";
                    bandwidth.setEnabled(true);

                }else{
                    JOptionPane.showMessageDialog(insideS11Panel, "Choose a " +
                            "resolution");
                }
            }
        });

        resolution.setName("Choose Resolution");



        bandwidth.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JComboBox c = (JComboBox)e.getSource();
                String wrd = (String)c.getSelectedItem();
                if(wrd.equals("600 MHz")){

//                    S11submittionstring = S11submittionstring + " 3e8";
                    bandwidthString = "3e8";
                    runS11Part1.setEnabled(true);

                }else if(wrd.equals("400 MHz")){

//                    S11submittionstring = S11submittionstring + " 2e8";
                    bandwidthString = "2e8";
                    runS11Part1.setEnabled(true);


                }else if(wrd.equals("200 MHz")){

//                    S11submittionstring = S11submittionstring + " 1e8";
                    bandwidthString = "1e8";
                    runS11Part1.setEnabled(true);


                }else{
                    JOptionPane.showMessageDialog(insideS11Panel, "Choose a " +
                            "bandwidth");
                }
            }
        });

        calculateBandwidth.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                ClassLoader classLoader = getClass().getClassLoader();
                File fi =
                        new File(classLoader.getResource("GuiS11_Part1").getFile());

                runCMD(new ProcessBuilder(fi.toString(), S11submittionstring,
                        resolutionString, bandwidthString));
            }
        });

        insideS11Panel.add(s11textField);
        insideS11Panel.add(submitfrequency);
        insideS11Panel.add(resolution);
        insideS11Panel.add(bandwidth);
        insideS11Panel.add(runS11Part1);
        insideS11Panel.add(runS11Part2);
        insideS11Panel.add(calculateBandwidth);
        insideS11Panel.add(S11ScrollPane);
        add(insideS11Panel);


    }


}
