import requests
import json

banner = """
╦ ╦┬ ┬┌┬┐┌─┐┌─┐┌┐┌╦═╗┌─┐┌─┐┬┌─  ╔═╗┌─┐┌─┐┬─┐┌─┐┬ ┬┌─┐┬─┐
╠═╣│ │ ││└─┐│ ││││╠╦╝│ ││  ├┴┐  ╚═╗├┤ ├─┤├┬┘│  ├─┤├┤ ├┬┘
╩ ╩└─┘─┴┘└─┘└─┘┘└┘╩╚═└─┘└─┘┴ ┴  ╚═╝└─┘┴ ┴┴└─└─┘┴ ┴└─┘┴└─
"""

def send_request_and_parse_response(email):
    url = 'https://cavalier.hudsonrock.com/api/json/v2/search-by-login'
    headers = {
        'api-key': 'ROCKHUDSONROCK',
        'Content-Type': 'application/json'
    }
    data = json.dumps({"login": email})

    response = requests.post(url, headers=headers, data=data)
    if response.status_code != 200:
        return f"Error: {response.status_code}"

    response_data = response.json()
    
    if not response_data:
        return "No leakages found"

    leaked_password_count = 0
    leaked_cookie_count = 0
    compromised_personal_services_count = 0
    compromised_corporate_services_count = 0

    purple = "\033[95m"
    yellow = "\033[93m"
    endc = "\033[0m"

    for item in response_data:
        print(f"{purple}Stealer Family:{endc} {item.get('stealer_family', 'N/A')}")
        print(f"{purple}Date Uploaded:{endc} {item.get('date_uploaded', 'N/A')}")
        print(f"{purple}Date Compromised:{endc} {item.get('date_compromised', 'N/A')}")
        print(f"{purple}Computer Name:{endc} {item.get('computer_name', 'N/A')}")
        print(f"{purple}Operating System:{endc} {item.get('operating_system', 'N/A')}\n")

        leaked_password_count += len(item.get("credentials", []))
        leaked_cookie_count += len(item.get("employee_session_cookies", []))
        compromised_personal_services_count += len(item.get("clientAt", []))
        compromised_corporate_services_count += len(item.get("employeeAt", []))

    output = f"{yellow}Total Leaked Passwords:{endc} {leaked_password_count}\n"
    output += f"{yellow}Number of Leaked Cookies:{endc} {leaked_cookie_count}\n"
    output += f"{yellow}Compromised Personal Services:{endc} {compromised_personal_services_count}\n"
    output += f"{yellow}Compromised Corporate Services:{endc} {compromised_corporate_services_count}"
    return output

print(banner)
print("Made with <3 by @jasonthename (GitHub)\n")
email_input = input("Please enter your email: ")
result = send_request_and_parse_response(email_input)
print(result)