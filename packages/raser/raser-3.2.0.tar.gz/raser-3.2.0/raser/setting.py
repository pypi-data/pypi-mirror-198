# -*- encoding: utf-8 -*-

'''
Description: Raser parameter settings      
@Date       : 2021/09/02 09:57:00
@Author     : tanyuhang
@version    : 1.0
'''
import json
import random

# Define all input parameters used in raser main process
class Setting:
    def __init__(self,parameters):
        """
        Description:
            1.Different functions detector(), fenics(), pygeant4() define 
            different class parameters.
            2.Parameter defined according input parameters.
        Parameters:
        ---------
        det_model : str
            Define the sensor models for simulation.eg. planar-3D plugin-3D
        _pardic : dictionaries
            Storage the input parameters
        laser_model : str
            Define the absorption pattern of laser
        @Modify:
        ---------
            2021/09/02
        """
        self._pardic = {}
        self.input2dic(parameters)
        self.det_name = self._pardic['det_name']
        self.read_par(self._pardic['parfile'])
        if "laser_model" in self._pardic:
            self.laser_model = self._pardic['laser_model']
            self.read_par_laser(self._pardic['laser_parfile'])
        
        p = self.paras
        self.total_events = int(p['total_events'])
        #self.g4seed = 0 
        self.g4seed = random.randint(0,1e7)

    def input2dic(self,parameters):
        " Transfer input list to dictinary"
        for par in parameters:
            name,_,value=par.rpartition('=')
            self._pardic[name]=value

    def read_par(self,jsonfile):
        "Read the setting.json file and save the input parameters in paras"
        with open(jsonfile) as f:
            dic_pars = json.load(f)
        for dic_par in dic_pars:
            if self.det_name == dic_par['det_name']:
                self.det_model = dic_par['det_model']
                paras = dic_par
        for x in paras: 
            if self.is_number(paras[x]):          
                paras[x] = float(paras[x])
            else:
                paras[x] = paras[x]
        self.paras = paras

    def read_par_laser(self,jsonfile):
        "Read the laser_setting.json file and save the input parameters in paras"
        with open(jsonfile) as f:
            dic_pars = json.load(f)
        for dic_par in dic_pars:
            if dic_par['laser_model'] in self.laser_model:
                laser_paras = dic_par
        for x in laser_paras: 
            if self.is_number(laser_paras[x]):          
                laser_paras[x] = float(laser_paras[x])
            else:
                laser_paras[x] = laser_paras[x]
        self.laser_paras = laser_paras

    @property
    def detector(self):
        """
        Description:
            Define different types detectors parameters. 
            Like: planar3D, plugin3D, lgad3D
        Parameters:
        ---------
        lx,ly,lz : float
            Detector length, width and height
        doping : float
            Doping concentation should times 1e12 /um^3  
            -- N-type is positive (negetive volatge applied) 
            -- P-type is negetive (positive volatge applied)
        temp : float
            Tempareture
        steplength : float
            The length of single step for e-h pairs to drift
        e_r : float
            Radius of electrode in 3D
        e_gap : float
            Spacing between the electrodes in 3D
        @Returns:
        ---------
            A dictionary containing all parameters used in detector  
        @Modify:
        ---------
            2021/09/02
        """
        p = self.paras
        if "planar3D" in self.det_model:
            detector = {'det_model':'planar3D', 'lx':p['lx'], 'ly':p['ly'], 'lz':p['lz'], 
                        'material':p['material'], 'voltage':p['voltage'], 'temp':p['temp'],
                        'doping':p['doping'], 'steplength':p['steplength']
                        }
            
        if "planarRing" in self.det_model:
            detector = {'det_model':'planarRing', 'lx':p['lx'], 'ly':p['ly'], 'lz':p['lz'], 
                        'e_r_inner':p['e_r_inner'],'e_r_outer':p['e_r_outer'],
                        'material':p['material'], 'voltage':p['voltage'], 'temp':p['temp'],
                        'doping':p['doping'], 'steplength':p['steplength']
                        }
            
        if "plugin3D" in self.det_model:
            detector = {'det_model':'plugin3D', 'lx':p['lx'], 'ly':p['ly'], 'lz':p['lz'],
                        'material':p['material'],'voltage':p['voltage'], 'temp':p['temp'], 
                        'doping':p['doping'], 'steplength':p['steplength'],
                        'e_r':p['e_r'], 'e_gap':p['e_gap'], 'custom_electrode': p['custom_electrode']
                        }
        if "lgad3D" in self.det_model:
            if p['part']==2:
                detector = {'det_model':'lgad3D', 'lx':p['lx'], 'ly':p['ly'], 'lz':p['lz'],
                            'material':p['material'], 'voltage':p['voltage'], 'temp':p['temp'],
                            'part':p['part'], 'avalanche_bond':p['avalanche_bond'], 
                            'doping1':p['doping1'], 'doping2':p['doping2'],
                            'steplength':p['steplength'], 'avalanche_model':p['avalanche_model']
                            }
            if p['part']==3:
                detector = {'det_model':'lgad3D', 'lx':p['lx'], 'ly':p['ly'], 'lz':p['lz'],
                            'material':p['material'], 'voltage':p['voltage'], 'temp':p['temp'],
                            'part':p['part'], 'control_bond':p['control_bond'], 'avalanche_bond':p['avalanche_bond'], 
                            'doping1':p['doping1'],'doping2':p['doping2'], 'doping3':p['doping3'],
                            'steplength':p['steplength'], 'avalanche_model':p['avalanche_model']
                            }
        return detector

    def electron_custom(self,electrodes):
        self.electrodes = electrodes

    @property
    def electron_customs(self):
        return self.electrodes
        
    @property
    def fenics(self):
        """
        Description:
            Define different fenics parameters
        Parameters:
        ---------
        mesh : int
            Mesh precision value, the bigger the higher the accuracy
        xyscale : int
            In plane detector, scale_xy is scaling sensor 50 times at x and 
            y axis, so the precision can improve 50 times in echo distance
        @Returns:
        ---------
            A dictionary containing all parameters used in fenics  
        @Modify:
        ---------
            2022/05/15
        """
        p = self.paras
        if "planar3D" in self.det_model:
            fenics = {'det_model':'planar3D', 
                      'mesh':p['mesh'], "xyscale":p['xyscale']}
        if "planarRing" in self.det_model:
            fenics = {'det_model':'planarRing', 
                      'mesh':p['mesh'], "xyscale":p['xyscale']}
        if "lgad3D" in self.det_model:
            fenics = {'det_model':'lgad3D',
                      'mesh':p['mesh'], "xyscale":p['xyscale']}
        if "plugin3D" in self.det_model:
            fenics = {'det_model':'plugin3D', 
                      'mesh':p['mesh'], "xyscale":p['xyscale']}
        return fenics

    @property
    def pygeant4(self):
        """
        Description:
            Define different geant4 parameters
        Parameters:
        ---------
        maxstep : float
            Simulate the step size of each step in Geant4
        par_in : list
            Incident particle position
        par_out : list
            Theoretical position of outgoing particles
        g4_vis : bool
            False: Graphical interface of geant4 particles Disabled
            True: Graphical interface of geant4 particles Enabled
        @Returns:
        ---------
            A dictionary containing all parameters used in geant4  
        @Modify:
        ---------
            2021/09/02
        """
        p = self.paras
        pygeant4 = {'det_model':self.det_model,
                    'maxstep':p['maxstep'], 'g4_vis':p['g4_vis'],
                    'par_in':[p['par_inx'], p['par_iny'], p['par_inz']], 
                    "par_out":[p['par_outx'], p['par_outy'], p['par_outz']],
                    }
        return pygeant4

    @property
    def laser(self):
        """
        Description:
            Define laser parameters
        
        Parameters:
        ---------
        tech : str
            Interaction Pattern Between Laser and Detector
        direction : str
            Direction of Laser Incidence, Could be "top" "edge" or "bottom"

        alpha : float
            the Linear Absorption Coefficient of the Bulk of the Device
        beta_2 : float
            the Quadratic Absorption Coefficient of the Bulk of the Device
        refractionIndex :float
            the Refraction Index of the Bulk of the Device

        wavelength : float
            the Wavelength of Laser in nm
        tau : float
            the Full-width at Half-maximum (FWHM) of the Beam Temporal Profile
        power : float
            the Energy per Laser Pulse
        widthBeamWaist : float
            the Width of the Beam Waist of the Laser in um
        l_Rayleigh : float
            the Rayleigh Width of the Laser Beam

        r_step, h_step : float
            the Step Length of Block in um,
            Carriers Generated in the Same Block Have the Same Drift Locus
        
        @Returns:
        ---------
            A dictionary containing all parameters used in TCTTracks
        
        @Modify:
        ---------
            2021/09/08
        """
        if hasattr(self,"laser_model"):
            p = self.laser_paras
            laser = {'tech':p['tech'],'direction':p['direction'],
                    'refractionIndex':p['refractionIndex'],
                    "wavelength":p["wavelength"],"tau":p["tau"],"power":p["power"],"widthBeamWaist":p["widthBeamWaist"],
                    'r_step':p['r_step'],'h_step':p['h_step'],
                    'fx_rel':p['fx_rel'],'fy_rel':p['fy_rel'],'fz_rel':p['fz_rel'],
                    }
            if p['tech'] == "SPA":
                laser.update({'alpha':p['alpha']})
            if p['tech'] == "TPA":
                laser.update({'beta_2':p['beta_2']})
            if 'l_Rayleigh' in p:
                laser.update({'l_Rayleigh':p['l_Rayleigh']})
        return laser
        
    @property
    def amplifier(self):
        """
        Description:
            Define diffrenet amplifiers parameters
        Parameters:
        ---------
        t_rise : 
        t_fall :
        trans_imp :
        CDet :

        BBW : 
        BBGain :
        BB_imp :
        OscBW :

        @Returns:
        ---------
            Two dictionary containing all parameters used for two types of amplifiers:
            current sensitive (CSA) and charge sensitive (BB)
        @Modify:
        ---------
            2021/09/02
        """
        p = self.paras
        CSA_par = {'name':'CSA_ampl', 't_rise':p['t_rise'], 
                   't_fall':p['t_fall'], 'trans_imp':p['trans_imp'], 
                   'CDet':p['CDet']
                  }
        BB_par = {'name':'BB_ampl', 'BBW':p['BBW'], 
                  'BBGain':p['BBGain'], 'BB_imp':p['BB_imp'],'OscBW':p['OscBW']
                 }
        return [CSA_par,BB_par]

    def scan_variation(self):
        " Define parameters of batch mode"
        self.total_events = int(self._pardic['total_e'])
        self.instance_number = int(self._pardic['instan'])
        self.g4seed = self.instance_number * self.total_events
        self.output = self._pardic["output"]

    def is_number(self,s):
        "Define whether the s is a number or not"
        try:
            float(s)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False 
