"""
OBD-II diagnostic trouble codes database and lookup functionality.
Contains comprehensive database of OBD codes with descriptions, causes, and fixes.
"""

class OBDDatabase:
    """Database of OBD-II diagnostic trouble codes."""
    
    def __init__(self):
        """Initialize the OBD codes database."""
        self.codes = {
            # P0xxx - Powertrain codes
            "P0300": {
                "description": "Random/Multiple Cylinder Misfire Detected",
                "severity": "High",
                "causes": [
                    "Faulty spark plugs or ignition coils",
                    "Vacuum leaks in intake manifold",
                    "Low fuel pressure or clogged fuel injectors",
                    "Carbon buildup on valves",
                    "Worn piston rings or valve guides"
                ],
                "fixes": [
                    "Replace spark plugs and check ignition coils",
                    "Inspect and repair vacuum lines",
                    "Clean or replace fuel injectors",
                    "Check fuel pressure and replace fuel filter",
                    "Perform compression test if issue persists"
                ]
            },
            "P0301": {
                "description": "Cylinder 1 Misfire Detected",
                "severity": "High",
                "causes": [
                    "Faulty spark plug in cylinder 1",
                    "Bad ignition coil for cylinder 1",
                    "Clogged fuel injector in cylinder 1",
                    "Low compression in cylinder 1",
                    "Vacuum leak affecting cylinder 1"
                ],
                "fixes": [
                    "Replace spark plug for cylinder 1",
                    "Test and replace ignition coil if needed",
                    "Clean or replace fuel injector",
                    "Check compression and repair if low",
                    "Inspect vacuum lines near cylinder 1"
                ]
            },
            "P0302": {
                "description": "Cylinder 2 Misfire Detected",
                "severity": "High",
                "causes": [
                    "Faulty spark plug in cylinder 2",
                    "Bad ignition coil for cylinder 2",
                    "Clogged fuel injector in cylinder 2",
                    "Low compression in cylinder 2",
                    "Vacuum leak affecting cylinder 2"
                ],
                "fixes": [
                    "Replace spark plug for cylinder 2",
                    "Test and replace ignition coil if needed",
                    "Clean or replace fuel injector",
                    "Check compression and repair if low",
                    "Inspect vacuum lines near cylinder 2"
                ]
            },
            "P0171": {
                "description": "System Too Lean (Bank 1)",
                "severity": "Medium",
                "causes": [
                    "Vacuum leak in intake system",
                    "Faulty mass airflow sensor (MAF)",
                    "Clogged fuel filter or weak fuel pump",
                    "Dirty fuel injectors",
                    "Faulty oxygen sensor"
                ],
                "fixes": [
                    "Check for and repair vacuum leaks",
                    "Clean or replace MAF sensor",
                    "Replace fuel filter and test fuel pump",
                    "Clean fuel injectors",
                    "Test and replace oxygen sensors if needed"
                ]
            },
            "P0172": {
                "description": "System Too Rich (Bank 1)",
                "severity": "Medium",
                "causes": [
                    "Faulty oxygen sensor",
                    "Dirty mass airflow sensor",
                    "Leaking fuel injectors",
                    "High fuel pressure",
                    "Faulty coolant temperature sensor"
                ],
                "fixes": [
                    "Replace oxygen sensor",
                    "Clean MAF sensor",
                    "Test and replace leaking injectors",
                    "Check fuel pressure regulator",
                    "Test coolant temperature sensor"
                ]
            },
            "P0420": {
                "description": "Catalyst System Efficiency Below Threshold (Bank 1)",
                "severity": "Medium",
                "causes": [
                    "Faulty catalytic converter",
                    "Faulty oxygen sensors",
                    "Engine misfiring",
                    "Oil or coolant contamination",
                    "Exhaust leak before catalytic converter"
                ],
                "fixes": [
                    "Replace catalytic converter",
                    "Replace upstream and downstream O2 sensors",
                    "Fix any engine misfires first",
                    "Check for oil/coolant leaks",
                    "Repair exhaust leaks"
                ]
            },
            "P0442": {
                "description": "Evaporative Emission Control System Leak Detected (Small Leak)",
                "severity": "Low",
                "causes": [
                    "Loose or faulty gas cap",
                    "Cracked EVAP lines or hoses",
                    "Faulty purge valve",
                    "Faulty vent valve",
                    "Small leak in fuel tank"
                ],
                "fixes": [
                    "Check and replace gas cap",
                    "Inspect and replace EVAP hoses",
                    "Test and replace purge valve",
                    "Test and replace vent valve",
                    "Perform smoke test to locate leak"
                ]
            },
            "P0505": {
                "description": "Idle Control System Malfunction",
                "severity": "Medium",
                "causes": [
                    "Faulty idle air control valve",
                    "Carbon buildup in throttle body",
                    "Vacuum leaks",
                    "Faulty throttle position sensor",
                    "Dirty air filter"
                ],
                "fixes": [
                    "Clean or replace idle air control valve",
                    "Clean throttle body",
                    "Check for vacuum leaks",
                    "Test throttle position sensor",
                    "Replace air filter"
                ]
            },
            "P0128": {
                "description": "Coolant Thermostat (Coolant Temperature Below Thermostat Regulating Temperature)",
                "severity": "Low",
                "causes": [
                    "Faulty thermostat stuck open",
                    "Low coolant level",
                    "Faulty coolant temperature sensor",
                    "Radiator fan running constantly",
                    "Air in cooling system"
                ],
                "fixes": [
                    "Replace thermostat",
                    "Check and refill coolant",
                    "Test coolant temperature sensor",
                    "Check radiator fan operation",
                    "Bleed air from cooling system"
                ]
            },
            
            # B0xxx - Body codes
            "B0001": {
                "description": "Driver Airbag Circuit Malfunction",
                "severity": "High",
                "causes": [
                    "Faulty airbag module",
                    "Damaged wiring harness",
                    "Bad airbag clock spring",
                    "Corroded connections",
                    "Faulty airbag control module"
                ],
                "fixes": [
                    "Have airbag system professionally diagnosed",
                    "Replace faulty airbag components",
                    "Repair wiring connections",
                    "Replace clock spring if needed",
                    "Do not attempt DIY repairs on airbag systems"
                ]
            },
            
            # C0xxx - Chassis codes
            "C0040": {
                "description": "Right Front Wheel Speed Sensor Circuit Malfunction",
                "severity": "Medium",
                "causes": [
                    "Faulty wheel speed sensor",
                    "Damaged sensor wiring",
                    "Dirty or damaged tone ring",
                    "Corroded sensor connections",
                    "Faulty ABS control module"
                ],
                "fixes": [
                    "Replace wheel speed sensor",
                    "Repair damaged wiring",
                    "Clean or replace tone ring",
                    "Clean sensor connections",
                    "Test ABS control module"
                ]
            },
            
            # U0xxx - Network codes
            "U0100": {
                "description": "Lost Communication With ECM/PCM",
                "severity": "High",
                "causes": [
                    "Faulty ECM/PCM",
                    "Damaged CAN bus wiring",
                    "Corroded connections",
                    "Low system voltage",
                    "Faulty body control module"
                ],
                "fixes": [
                    "Check all fuses and relays",
                    "Test CAN bus network",
                    "Check battery and charging system",
                    "Inspect wiring connections",
                    "Professional ECM/PCM diagnosis required"
                ]
            }
        }
    
    def lookup_code(self, code: str):
        """
        Look up an OBD code and return detailed information.
        
        Args:
            code: OBD code (e.g., 'P0301', 'p0301', or '0301')
            
        Returns:
            Dictionary with code information or None if not found
        """
        # Normalize the code
        code = code.upper().strip()
        
        # Add 'P' prefix if missing and it's a 4-digit number
        if len(code) == 4 and code.isdigit():
            code = 'P' + code
        
        return self.codes.get(code)
    
    def search_codes(self, keyword: str) -> list:
        """
        Search for codes containing a keyword in description.
        
        Args:
            keyword: Search term
            
        Returns:
            List of matching codes
        """
        keyword = keyword.lower()
        matches = []
        
        for code, info in self.codes.items():
            if keyword in info['description'].lower():
                matches.append({
                    'code': code,
                    'description': info['description']
                })
        
        return matches
    
    def get_all_codes(self) -> list:
        """Get list of all available codes."""
        return list(self.codes.keys())
    
    def get_codes_by_severity(self, severity: str) -> list:
        """Get codes filtered by severity level."""
        severity = severity.lower().capitalize()
        return [code for code, info in self.codes.items() 
                if info.get('severity', '').lower() == severity.lower()]