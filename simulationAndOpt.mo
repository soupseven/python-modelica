package simulationAndOpt
  model system
  parameter Real x=1;
  parameter Real y=1;
  Real energy;
  equation
  energy=Modelica.Math.sin(x)+Modelica.Math.cos(y)*Modelica.Constants.e^(-(x^2+y^2));
  annotation(
      Documentation(info = "<html><head></head><body><br></body></html>"));
  end system;
end simulationAndOpt;
