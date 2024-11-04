from time_utils import TimeUtils

class Formatter:
    def __init__(self):
        pass
    
    def formatWeatherDataHtml1(self, vals):
        message1 = f"""
                        <html>
                        <head>
                            <style>
                                body {{
                                    font-family: 'Arial', sans-serif;
                                    background-color: #f4f4f4;
                                    color: #333;
                                }}
                                table {{
                                    width: 80%;
                                    margin: 20px auto;
                                    border-collapse: collapse;
                                    border: 1px solid #ddd;
                                }}
                                th, td {{
                                    padding: 12px;
                                    text-align: left;
                                    border-bottom: 1px solid #ddd;
                                }}
                                th {{
                                    background-color: #f2f2f2;
                                }}
                            </style>
                        </head>
                        <body>

                        <h2>Weather Information</h2>

                        <table>
                            <tr>
                                <th>Data & Time</th>
                                <td>{vals[0]}</td>
                            </tr>
                            <tr>
                                <th>Sunrise</th>
                                <td>{vals[1]}</td>
                            </tr>
                            <tr>
                                <th>Sunset</th>
                                <td>{vals[2]}</td>
                            </tr>
                            <tr>
                                <th>Temperature</th>
                                <td>{vals[3]}</td>
                            </tr>
                            <tr>
                                <th>Feels Like</th>
                                <td>{vals[4]}</td>
                            </tr>
                            <tr>
                                <th>Pressure</th>
                                <td>{vals[5]}</td>
                            </tr>
                            <tr>
                                <th>Humidity</th>
                                <td>{vals[6]}</td>
                            </tr>
                            <tr>
                                <th>Dew Point</th>
                                <td>{vals[7]}</td>
                            </tr>
                            <tr>
                                <th>UV Index</th>
                                <td>{vals[8]}</td>
                            </tr>
                            <tr>
                                <th>Clouds</th>
                                <td>{vals[9]}</td>
                            </tr>
                            <tr>
                                <th>Visibility</th>
                                <td>{vals[10]}</td>
                            </tr>
                            <tr>
                                <th>Wind Speed</th>
                                <td>{vals[11]}</td>
                            </tr>
                            <tr>
                                <th>Wind Degree</th>
                                <td>{vals[12]}</td>
                            </tr>
                        </table>

                        </body>
                        </html>
                        """
        return message1
       
    def formatWeatherDataHtml2(self, vals):
        message2 = f"""
                    <html>
                    <head>
                        <style>
                            body {{
                                font-family: 'Arial', sans-serif;
                                background-color: #eff8ff;
                                color: #333;
                                margin: 20px;
                            }}
                            .report-container {{
                                max-width: 600px;
                                margin: 0 auto;
                                padding: 20px;
                                border: 2px solid #3498db;
                                border-radius: 10px;
                                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                                background-color: #fff;
                            }}
                            .highlight {{
                                color: #e74c3c;
                                font-weight: bold;
                            }}
                            .important {{
                                background-color: #f8d7da;
                                padding: 2px;
                                color: #721c24;
                                border-radius: 3px;
                            }}
                        </style>
                    </head>
                    <body>

                    <div class="report-container">
                        <h2>Weather Report</h2>
                        <h3>Good Morning, {self.greet['Name']}</h3>

                        <p>
                            The current weather report for <span class="highlight">{vals[0]}</span> at  <span class="highlight">{self.greet['Location']}</span> is as follows:
                        </p>

                        <p>
                            <strong>Sunrise:</strong> {vals[1]} | <strong>Sunset:</strong> {vals[2]}
                        </p>

                        <p>
                            The temperature is <span class="highlight">{vals[3]}</span>, and it feels like <span class="highlight">{vals[4]}</span>. The atmospheric pressure is <span class="highlight">{vals[5]}</span>,
                            humidity is <span class="highlight">{vals[6]}</span>, and the dew point is <span class="highlight">{vals[7]}</span>.
                        </p>

                        <p>
                            The UV Index is <span class="highlight">{vals[8]}</span>, clouds cover <span class="highlight">{vals[9]}</span> of the sky, and visibility is <span class="highlight">{vals[10]}</span>.
                        </p>

                        <p>
                            Wind speed is <span class="highlight">{vals[11]}</span>, coming from <span class="highlight">{vals[12]}</span> degrees.
                        </p>
                        <p> Have a nice day! </p>
                        <p> <em> Location not correct? Reply to this mail with correct location. </em> </p>
                    </div>

                    </body>
                    </html>
                    """
    
        return message2
    
    def formatWeatherDataHtmlEmail(self,data_list, day_list, name, location):
        html_content = '<html>\n<head>\n<style>\n' \
                    'body { font-family: Arial, sans-serif; background-color: #f0f8ff; }\n' \
                    '.container { max-width: 800px; margin: 20px auto; padding: 20px; background-color: #fff; box-shadow: 0 0 10px rgba(0,0,0,0.1); border-radius: 10px; }\n' \
                    '.weather-card { border: 1px solid #ccc; border-radius: 5px; padding: 15px; margin-bottom: 20px; background-color: #f9f9f9; }\n' \
                    '.weather-header { font-size: 20px; font-weight: bold; margin-bottom: 10px; color: #333; }\n' \
                    '.weather-details { margin-left: 15px; }\n' \
                    '.weather-details p { margin: 5px 0; }\n' \
                    '.weather-details ul { list-style-type: none; padding: 0; }\n' \
                    '.weather-details ul li { margin-bottom: 5px; }\n' \
                    '.summary { color: #1e90ff; font-weight: bold; }\n' \
                    '.temp { color: #2e8b57; }\n' \
                    '.sunrise-sunset { color: #ffa500; }\n' \
                    '.wind { color: #4682b4; }\n' \
                    '.uv-index { color: #ff6347; }\n' \
                    '.greeting { background-color: #1e90ff; color: #fff; padding: 10px; border-radius: 5px; margin-bottom: 20px; }\n' \
                    '</style>\n</head>\n<body>\n'

        html_content += f'''<div class="container">\n<div class="greeting">'''
        html_content += '''<h2 style="margin-top: 0;">Weather Report</h2>\n'''
        html_content += f'''<h3 style="margin-top: 0;">Good Morning, {str(name).title()}</h3>\n'''
        html_content += f'''<p>Weather Forecast for Today at<br><b>{str(location).title()}</b></p>\n'''
        html_content += '</div>\n'

        for day_data in [data_list]:
            html_content += '<div class="weather-card">\n'
            html_content += f'<div class="weather-header">{TimeUtils().timestamp_to_date(day_data["dt"])}</div>\n'
            html_content += '<div class="weather-details">\n'
            html_content += f'<p class="summary">Summary: {day_data["summary"]}</p>\n'
            html_content += '<ul>\n'
            html_content += f'<li class="sunrise-sunset">Sunrise: {TimeUtils().timestamp_to_time(day_data["sunrise"])}</li>\n'
            html_content += f'<li class="sunrise-sunset">Sunset: {TimeUtils().timestamp_to_time(day_data["sunset"])}</li>\n'
            html_content += f'<li class="temp">Temperature: Day: {day_data["temp"]["day"]} °C, Night: {day_data["temp"]["night"]} °C</li>\n'
            html_content += f'<li class="temp">Feels Like: Day: {day_data["feels_like"]["day"]} °C, Night: {day_data["feels_like"]["night"]} °C</li>\n'
            html_content += f'<li>Humidity: {day_data["humidity"]} %</li>\n'
            html_content += f'<li class="wind">Wind: {day_data["wind_speed"]} m/s, {day_data["wind_deg"]}°</li>\n'
            html_content += f'<li class="uv-index">UV Index: {day_data["uvi"]}</li>\n'
            html_content += '</ul>\n'
            html_content += '</div>\n'
            html_content += '</div>\n'
        for hour in day_list[0:25]:
            html_content += '<div class="weather-card">\n'
            html_content += f'<div class="weather-header">{TimeUtils().timestamp_to_time(hour["dt"])}</div>\n'
            html_content += '<div class="weather-details">\n'
            html_content += f'<p class="summary">{hour["weather"][0]["description"].title()}</p>\n'
            html_content += '<ul>\n'
            html_content += f'<li class="temp">Temperature: {hour["temp"]} °C, Feels Like: {hour["feels_like"]} °C</li>\n'
            html_content += f'<li>Humidity: {hour["humidity"]} %</li>\n'
            html_content += f'<li class="wind">Wind: {hour["wind_speed"]} m/s, {hour["wind_deg"]}°</li>\n'
            html_content += f'<li class="uv-index">UV Index: {hour["uvi"]}</li>\n'
            html_content += f'<li class="uv-index">Clouds cover {hour["clouds"]}% of the sky</li>\n'
            html_content += '</ul>\n'
            html_content += '</div>\n'
            html_content += '</div>\n'
        html_content += '''<p> Have a nice day! </p><p> <em> Location not correct? Reply to this mail with correct location. </em> </p>'''
        html_content += '</div>\n'
        html_content += '</body>\n</html>'

        return html_content
    
    def formatWeatherDataHtmlTableEmail(self,data_list, day_list, name, location):
        html_content = '''<html>
        <head>
        <style>
        body { font-family: Arial, sans-serif; background-color: #f0f8ff; }
        .container { max-width: 800px; margin: 20px auto; padding: 20px; background-color: #fff; box-shadow: 0 0 10px rgba(0,0,0,0.1); border-radius: 10px; }
        .weather-card { border: 1px solid #ccc; border-radius: 5px; padding: 15px; margin-bottom: 20px; background-color: #f9f9f9; }
        .weather-header { font-size: 20px; font-weight: bold; margin-bottom: 10px; color: #333; }
        .weather-details { margin-left: 15px; }
        .weather-details p { margin: 5px 0; }
        .weather-details ul { list-style-type: none; padding: 0; }
        .weather-details ul li { margin-bottom: 5px; }
        .summary { color: #1e90ff; font-weight: bold; }
        .temp { color: #2e8b57; }
        .sunrise-sunset { color: #ffa500; }
        .wind { color: #4682b4; }
        .uv-index { color: #ff6347; }
        .greeting { background-color: #1e90ff; color: #fff; padding: 10px; border-radius: 5px; margin-bottom: 20px; }
        table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        tr:nth-child(odd) { background-color: #fff; }
        </style>
        </head>
        <body>
        '''

        html_content += f'''<div class="container">
        <div class="greeting">
        <h2 style="margin-top: 0;">Weather Report</h2>
        <h3 style="margin-top: 0;">Good Morning, {str(name).title()}</h3>
        <p>Weather Forecast for Today at<br><b>{str(location).title()}</b></p>
        </div>
        '''

        html_content += '<div class="weather-card">\n'
        html_content += f'<div class="weather-header">{TimeUtils().timestamp_to_date(data_list["dt"])}</div>\n'
        html_content += '<div class="weather-details">\n'
        html_content += f'<p class="summary">Summary: {data_list["summary"]}</p>\n'
        html_content += '<table>\n'
        html_content += '<tr><th>Sunrise</th><th>Sunset</th><th>Temp Day</th><th>Temp Night</th><th>Feels Like Day</th><th>Feels Like Night</th><th>Humidity</th><th>Wind</th><th>UV Index</th></tr>\n'
        html_content += f'<tr><td class="sunrise-sunset">{TimeUtils().timestamp_to_datetime(data_list["sunrise"])}</td>'
        html_content += f'<td class="sunrise-sunset">{TimeUtils().timestamp_to_datetime(data_list["sunset"])}</td>'
        html_content += f'<td class="temp">{data_list["temp"]["day"]} °C</td>'
        html_content += f'<td class="temp">{data_list["temp"]["night"]} °C</td>'
        html_content += f'<td class="temp">{data_list["feels_like"]["day"]} °C</td>'
        html_content += f'<td class="temp">{data_list["feels_like"]["night"]} °C</td>'
        html_content += f'<td>{data_list["humidity"]} %</td>'
        html_content += f'<td class="wind">{data_list["wind_speed"]} m/s, {data_list["wind_deg"]}°</td>'
        html_content += f'<td class="uv-index">{data_list["uvi"]}</td></tr>\n'
        html_content += '</table>\n'
        html_content += '</div>\n'
        html_content += '</div>\n'

        html_content += '<div class="weather-card">\n'
        html_content += '<div class="weather-header">Hourly Forecast For Next 24 Hours</div>\n'
        html_content += '<div class="weather-details">\n'
        html_content += '<table>\n'
        html_content += '<tr><th>Time</th><th>Summary</th><th>Temp</th><th>Feels Like</th><th>Humidity</th><th>Wind</th><th>UV Index</th><th>Clouds (% of sky)</th></tr>\n'
        for hour in day_list:
            html_content += f'<tr><td>{TimeUtils().timestamp_to_time(hour["dt"])}</td>'
            html_content += f'<td class="summary">{hour["weather"][0]["description"].title()}</td>'
            html_content += f'<td class="temp">{hour["temp"]} °C</td>'
            html_content += f'<td class="temp">{hour["feels_like"]} °C</td>'
            html_content += f'<td>{hour["humidity"]} %</td>'
            html_content += f'<td class="wind">{hour["wind_speed"]} m/s, {hour["wind_deg"]}°</td>'
            html_content += f'<td class="uv-index">{hour["uvi"]}</td>'
            html_content += f'<td class="uv-index">{hour["clouds"]}%</td></tr>\n'
        html_content += '</table>\n'
        html_content += '</div>\n'
        html_content += '</div>\n'

        html_content += '''<p> Have a nice day! </p><p> <em> Location not correct? Reply to this mail with correct location. </em> </p>'''
        html_content += '</div>\n'
        html_content += '</body>\n</html>'

        return html_content

        