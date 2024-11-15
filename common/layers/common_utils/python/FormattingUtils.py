from datetime import datetime
from DatetimeUtils import CommonUtils


class Formatter:
    def __init__(self):
        pass

    def running_html(self, running_data):
        return f"""
        <h3 class="section-title">Running ({running_data['formatted_date']})</h3> 
        <div style="text-align: center; margin-bottom: 20px;">
        <img src="{running_data['mapUrl']}" alt="Running Map" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px; display: block; margin: 0 auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
            </div>
        <div style="text-align: left; margin-bottom: 20px;">
        <h2 style="font-weight: bold; color: #00bfa5;">Streak: {running_data['streak']} Days</h2>
    </div>
        <table style="width:100%; border-collapse: collapse; text-align: left;">
            <tr>
                <th style="border-bottom: 1px solid #ddd; padding: 8px;">Metric</th>
                <th style="border-bottom: 1px solid #ddd; padding: 8px;">Value</th>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Activity Name</strong></td>
                <td style="padding: 8px;">{running_data['activity_name']}</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Start Time</strong></td>
                <td style="padding: 8px;">{running_data['formatted_start_time']}</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Distance</strong></td>
                <td style="padding: 8px;">{running_data['distance']:.2f} km</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Duration</strong></td>
                <td style="padding: 8px;">{running_data['duration']}</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Average Pace</strong></td>
                <td style="padding: 8px;">{running_data['avg_pace']}</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Best Pace</strong></td>
                <td style="padding: 8px;">{running_data['max_pace']}</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Calories Burned</strong></td>
                <td style="padding: 8px;">{running_data['calories']} kcal</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Avg HR</strong></td>
                <td style="padding: 8px;">{running_data['avg_hr']} bpm</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Max HR</strong></td>
                <td style="padding: 8px;">{running_data['max_hr']} bpm</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Avg Cadence</strong></td>
                <td style="padding: 8px;">{running_data['avg_cadence']} spm</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Max Cadence</strong></td>
                <td style="padding: 8px;">{running_data['max_cadence']} spm</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Stride Length</strong></td>
                <td style="padding: 8px;">{running_data['stride_length']} m</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Training Effect</strong></td>
                <td style="padding: 8px;">{running_data['training_effect']}</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Training Load</strong></td>
                <td style="padding: 8px;">{running_data['training_load']}</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Ground Contact Time</strong></td>
                <td style="padding: 8px;">{running_data['ground_contact_time']}</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Shoes</strong></td>
                <td style="padding: 8px;">{running_data['gear']}</td>
            </tr>
        </table>
        """

    def running_text(self, running_data):
        return f"""
Running ({running_data['formatted_date']})
=========================
Streak: {running_data['streak']} Days
{running_data['activity_name']}
{running_data['formatted_start_time']}
Distance: {running_data['distance']:.2f} kms
Duration: {running_data['duration']}
Avg Pace: {running_data['avg_pace']}
Best Pace: {running_data['max_pace']}
Calories: {running_data['calories']} kcal
Avg HR: {running_data['avg_hr']} bpm
Max HR: {running_data['max_hr']} bpm
Avg Cadence: {running_data['avg_cadence']} spm
Max Cadence: {running_data['max_cadence']} spm
Stride Length: {running_data['stride_length']} m
Training Effect: {running_data['training_effect']}
Training Load: {running_data['training_load']}
Ground Contact Time: {running_data['ground_contact_time']}
Shoes: {running_data['gear']}
"""

    def sleep_html(self, sleep_data):
        return f"""
            <h3 class="section-title">Sleep ({sleep_data['formatted_date']})</h3>
            <table class="data-table">
                <tr><th>Overall Sleep Summary</th></tr>
                <tr><td>You slept for {sleep_data['total_time']}, from {sleep_data['from_']} to {sleep_data['to_']}</td></tr>
                <tr><td>Score: <span class="score">{sleep_data['sleep_score']} ({sleep_data['quality']})</span></td></tr>
                <tr><td>Feedback: <span class="score">{sleep_data['Sleep Feedback']}</span></td></tr>
            </table>
            <table class="data-table">
                <tr><th>Sleep Stages</th><th>Quality</th><th>Time</th><th>Score</th><th>Optimal</th></tr>
                <tr><td>REM Sleep</td> <td>{sleep_data['REM_Quality']}</td><td>{sleep_data['REM_Time']}</td><td>{sleep_data['REM_Score']}</td><td>{sleep_data['REM_Optimal']}</td></tr>
                <tr><td>Light Sleep</td> <td>{sleep_data['Light_Quality']}</td><td>{sleep_data['Light_Time']}</td><td>{sleep_data['Light_Score']}</td><td>{sleep_data['Light_Optimal']}</td></tr>
                <tr><td>Deep Sleep</td> <td>{sleep_data['Deep_Quality']}</td><td>{sleep_data['Deep_Time']}</td><td>{sleep_data['Deep_Score']}</td><td>{sleep_data['Deep_Optimal']}</td></tr>
                <tr><td>Awake</td> <td>{sleep_data['Awake_Quality']}</td><td>{sleep_data['Awake_Time']}</td><td>{sleep_data['Awake_Score']}</td><td>{sleep_data['Awake_Optimal']}</td></tr>
            </table>
            <table class="data-table">
                <tr><th>Additional Metrics</th></tr>
                <tr><td>Avg Sleep Stress</td> <td>{sleep_data['Average_Sleep_Stress']}</td></tr>
                 <tr><td>Battery Change</td> <td>{sleep_data['Body Battery Change']}</td></tr>
                 <tr><td>Resting HR</td> <td>{sleep_data['Resting Heart Rate']}</td></tr>
                 <tr><td>Restlessness Level</td> <td>{sleep_data['Restlessness Level']}</td></tr>
            </table>
            """

    def sleep_text(self, sleep_data):
        return f"""
Sleep ({sleep_data['formatted_date']})
=========================
You slept for {sleep_data['total_time']}, from {sleep_data['from_']} to {sleep_data['to_']}.
Score: {sleep_data['sleep_score']} ({sleep_data['quality']})
Feedback: {sleep_data['Sleep Feedback']}
Sleep Stages:
-------------
REM: {sleep_data['REM_Quality']},{sleep_data['REM_Time']},{sleep_data['REM_Score']} [{sleep_data['REM_Optimal']}]
Light: {sleep_data['Light_Quality']},{sleep_data['Light_Time']},{sleep_data['Light_Score']} [{sleep_data['Light_Optimal']}]
Deep: {sleep_data['Deep_Quality']},{sleep_data['Deep_Time']},{sleep_data['Deep_Score']} [{sleep_data['Deep_Optimal']}]
Awake: {sleep_data['Awake_Quality']},{sleep_data['Awake_Time']},{sleep_data['Awake_Score']} [{sleep_data['Awake_Optimal']}]
Additional Metrics:
-------------------
Avg Sleep Stress: {sleep_data['Average_Sleep_Stress']}
Battery Change: {sleep_data['Body Battery Change']}
Resting HR: {sleep_data['Resting Heart Rate']}
Restlessness Level: {sleep_data['Restlessness Level']}
"""

    def body_stats_html(self, body_stats_data):
        return f"""
            <h3 class="section-title">Health ({body_stats_data['formatted_date']})</h3>
            <table class="data-table">
                <tr><th>Total Calories</th><td>{body_stats_data['Total kcal']}</td></tr>
                <tr><th>Active Calories</th><td>{body_stats_data['Active kcal']}</td></tr>
                <tr><th>Total Steps / Goal</th><td>{body_stats_data['Total Steps / Goal']}</td></tr>
                <tr><th>Distance</th><td>{round(body_stats_data['Distance']/1000,2)} kms</td></tr>
                <tr><th>Highly Active Duration</th><td>{body_stats_data['Highly Active Duration']}</td></tr>
                <tr><th>Moderate Intensity Duration</th><td>{body_stats_data['Moderate Intensity Minutes']} Minutes</td></tr>
                <tr><th>Floors Up</th><td>{body_stats_data['Floors Up']}</td></tr>
                <tr><th>Floors Down</th><td>{body_stats_data['Floors Down']}</td></tr>
                <tr><th>Heart Rate (Min/Resting/Max)</th><td>{body_stats_data['Heart Rate - Min/Resting/Max']}</td></tr>
                <tr><th>Last Seven Days Avg RHR</th><td>{body_stats_data["Last Seven Days Avg RHR"]}</td></tr>
                <tr><th>Average Stress</th><td>{body_stats_data['Avg Stress']}</td></tr>
                <tr><th>Max Stress</th><td>{body_stats_data["Max Stress"]}</td></tr>
                <tr><th>Blood Oxygen (SpO2)</th><td>{body_stats_data['Blood Oxygen (SpO2)']}</td></tr>
            </table>
            """

    def garminSleepFormatterForTelegram(self, d) -> str:
        try:
            summary_message = summary_message = (
                f"""{d['formatted_date']}\n\nSleep Statistics\nYou slept for {d['total_time']}, from {d['from_']} to {d['to_']}\nScore: {d['sleep_score']} ({d['quality']})\n\nREM Sleep: {d['REM_Quality']}\n\t\t\t\t{d['REM_Time']}\n\t\t\t\tScore: {d['REM_Score']} [Optimal: ({d['REM_Optimal']})\n\nLight Sleep: {d['Light_Quality']}\n\t\t\t\t{d['Light_Time']}\n\t\t\t\tScore: {d['Light_Score']} [Optimal: ({d['Light_Optimal']})]\n\nDeep Sleep: {d['Deep_Quality']}\n\t\t\t\t{d['Deep_Time']}\n\t\t\t\tScore: {d['Deep_Score']} [Optimal: ({d['Deep_Optimal']})]\n\nAwake: {d['Awake_Quality']}\n\t\t\t\t{d['Awake_Time']}\n\t\t\t\tScore: {d['Awake_Score']} [Optimal: ({d['Awake_Optimal']})]\n\nAverage Sleep Stress: {d["Average_Sleep_Stress"]}\nBody Battery Change: {d['Body Battery Change']}\nResting Heart Rate: {d['Resting Heart Rate']}\nRestlessness Level: {d['Restlessness Level']}\nRestless moments: {d['Restless moments']}\nSleep Feedback: {d["Sleep Feedback"]}"""
            )
        except Exception as e:
            summary_message = f"No Sleep Data in Garmin: {e}"
            print(summary_message)
        return summary_message

    def garminMainEmailFormatter(self, data, html_body):
        header_div = f"""<div class="header">
                <img src="{data['profile_image']}" class="profile-img" width="100" height="100">
                <div>
                    <h1>Garmin Statistics</h1>
                    <p><b>{data['user_name']}</b></p>
                </div>
            </div>""" 
        html_content = f"""
        <html>
        <head>
            <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #2d2d30;
            color: 	#3e3e42;
            padding: 20px;
            margin-bottom: 30px;
            line-height: 1.6;
        }}
        .header {{
            display: flex;
            align-items: center;
            margin-bottom: 30px;
            border-bottom: 2px solid #007acc;
            padding-bottom: 20px;
        }}
        .profile-img {{
            border-radius: 50%;
            margin-right: 20px;
            border: 3px solid #444;
            width: 80px;
            height: 80px;
        }}
        .header h1 {{
            font-size: 2.2em;
            color: #007acc;
            margin: 0;
        }}
        .header p {{
            font-size: 1.1em;
            color: #b0bec5;
        }}
        .summary {{
            background-color: #242424;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.6);
            margin-bottom: 30px;
            border: 1px solid #444;
        }}
        .summary span {{
            font-weight: bold;
            color: 	#3e3e42;
        }}
        .data-table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 30px;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #444;
            color: #cfd8dc;
        }}
        th {{
            background-color: #007acc;
            color: #fff;
            font-size: 1.1em;
            letter-spacing: 0.5px;
        }}
        td {{
            background-color: #202020;
            font-size: 0.95em;
        }}
        .section-title {{
            font-size: 1.8em;
            margin-bottom: 20px;
            color: #007acc;
            font-weight: bold;
            letter-spacing: 1px;
            text-transform: uppercase;
            border-bottom: 3px solid #007acc;
            padding-bottom: 10px;
        }}
        .footer {{
            text-align: center;
            color: #888;
            font-size: 0.85em;
            padding: 15px;
            border-top: 1px solid #444;
            margin-top: 30px;
        }}
        .footer img {{
            max-width: 100%;
            height: auto;
            margin-top: 15px;
        }}
        a {{
            color: #007acc;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        button {{
            background-color: #007acc;
            color: #181818;
            border: none;
            padding: 12px 20px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 1em;
            transition: background-color 0.3s ease;
        }}
        button:hover {{
            background-color: #005fa3;
        }}
        .additional-details p {{
            font-size: 0.9em;
            color: #b0bec5;
            margin-bottom: 10px;
        }}
        /* Animation for hover effects */
        th, td {{
            transition: background-color 0.3s ease, color 0.3s ease;
        }}
        tr:hover td {{
            background-color: #333;
            color: #fff;
        }}
        </style>

        </head>
        <body>
        {header_div}
            <div class="summary">
            {html_body}
            <div class="footer">
        <p></p>
        <img src="{data['device_image']}" class="profile-img" width="15" height="15">
        <p>Uploaded From: <b>{data['device_name']}</b></p>
    </div>
</body>
</html>
"""
        return html_content

    def garminBodystatsFormatterForTelegram(self, d):
        try:
            summary_message = f"""Body Statistics for {d['formatted_date']}:\n\nTotal kcal: {d['Total kcal']}\nActive kcal: {d['Active kcal']}\nTotal Steps / Goal: {d['Total Steps / Goal']}\nDistance: {d['Distance']}\nHighly Active Duration: {d['Highly Active Duration']}\nActive Duration: {d['Active Duration']}\nSedentary Duration: {d['Sedentary Duration']}\nModerate Intensity Minutes: {d['Moderate Intensity Minutes']}\nVigorous Intensity Minutes: {d['Vigorous Intensity Minutes']}\nIntensity Minutes Goal Status: {d['Intensity Minutes Goal Status']}\nFloors Up: {d['Floors Up']}\nFloors Down: {d['Floors Down']}\nHeart Rate - Min/Resting/Max: {d['Heart Rate - Min/Resting/Max']}\nLast 7 Days Avg Resting Heart Rate: {d['Last Seven Days Avg Resting Heart Rate']}\nAverage Stress: {d['Average Stress']}\nMax Stress Level: {d['Max Stress Level']}\nStress Duration: {d['Stress Duration']}\nBlood Oxygen (SpO2): {d['Blood Oxygen (SpO2)']}"""
        except Exception as e:
            summary_message = f"No Body Data in Garmin: {e}"
            print(summary_message)
        return summary_message

    def newsletterEmailFormatterHtml(self, sleep_data, body_stats_data):
        try:
            message = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.5">
                 <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    width: 100%;
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: #fff;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    border-radius: 8px;
                    margin-top: 20px;
                }}
                .header {{
                    background-color: #0073e6;
                    color: white;
                    padding: 10px 20px;
                    text-align: center;
                    border-radius: 8px 8px 0 0;
                }}
                .content {{
                    padding: 20px;
                }}
                .section {{
                    margin-bottom: 30px;
                }}
                .section-title {{
                    font-size: 1.4em;
                    margin-bottom: 10px;
                    color: #0073e6;
                }}
                .stats {{
                    margin-bottom: 20px;
                    border-top: 1px solid #ddd;
                    padding-top: 10px;
                }}
                .footer img {{
                    max-width: 100%;
                    width: 100%;
                    height: auto; 
                    margin-top: 10px;
                }}

                .footer {{
                    text-align: center;
                    color: #777;
                    font-size: 0.9em;
                    padding: 10px;
                    border-top: 1px solid #ddd;
                    margin-top: 20px;
                }}
                .data-table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-bottom: 20px;
                }}
                .data-table th,
                .data-table td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                    background-color: #fff;
                }}
                .data-table th {{
                    color: #333;
                }}
                .score {{
                    font-weight: bold;
                }}
            </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h2>Garmin Statistics</h2>
                    </div>
                    <div class="content">
                        <div class="section">
                            <h3 class="section-title">Sleep Data for {sleep_data['formatted_date']}</h3>
                            <div class="stats">
                                <table class="data-table">
                                    <tr>
                                        <th>Overall Sleep Summary</th>
                                    </tr>
                                    <tr>
                                        <td>You slept for {sleep_data['total_time']}, from {sleep_data['from_']} to {sleep_data['to_']}</td>
                                    </tr>
                                    <tr>
                                        <td>Score: <span class="score">{sleep_data['sleep_score']} ({sleep_data['quality']})</span></td>
                                    </tr>
                                </table>

                                <table class="data-table">
                                    <tr>
                                        <th>Sleep Stages</th>
                                    </tr>
                                    <tr>
                                        <td><strong>REM Sleep:</strong></td>
                                        <td>{sleep_data['REM_Quality']}</td>
                                        <td>{sleep_data['REM_Time']}</td>
                                        <td>Score: <span class="score">{sleep_data['REM_Score']} Optimal: {sleep_data['REM_Optimal']}</span></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Light Sleep:</strong></td>
                                        <td>{sleep_data['Light_Quality']}</td>
                                        <td>{sleep_data['Light_Time']}</td>
                                        <td>Score: <span class="score">{sleep_data['Light_Score']} Optimal: {sleep_data['Light_Optimal']}</span></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Deep Sleep:</strong></td>
                                        <td>{sleep_data['Deep_Quality']}</td>
                                        <td>{sleep_data['Deep_Time']}</td>
                                        <td>Score: <span class="score">{sleep_data['Deep_Score']} Optimal: {sleep_data['Deep_Optimal']}</span></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Awake:</strong></td>
                                        <td>{sleep_data['Awake_Quality']}</td>
                                        <td>{sleep_data['Awake_Time']}</td>
                                        <td>Score: <span class="score">{sleep_data['Awake_Score']} Optimal: {sleep_data['Awake_Optimal']}</span></td>
                                    </tr>
                                </table>

                                <div class="section">
                                    <div class="section-title">Additional Details</div>
                                    <div class="section-content">
                                        <p>Average Sleep Stress: {sleep_data['Average_Sleep_Stress']}</p>
                                        <p>Battery Change: {sleep_data['Body Battery Change']}</p>
                                        <p>Resting Heart Rate: {sleep_data['Resting Heart Rate']}</p>
                                        <p>Restlessness Level: {sleep_data['Restlessness Level']}</p>
                                        <p>Restless moments: {sleep_data['Restless moments']}</p>
                                        <p>Sleep Feedback: {sleep_data['Sleep Feedback']}</p>
                                    </div>
                                </div>
                            </div>

                            <div class="stats">
                                <h3 class="section-title">Body Statistics for {body_stats_data['formatted_date']}</h3>
                                <table class="data-table">
                                    <tr>
                                        <th>Total kcal</th>
                                        <td>{body_stats_data['Total kcal']}</td>
                                    </tr>
                                    <tr>
                                        <th>Active kcal</th>
                                        <td>{body_stats_data['Active kcal']}</td>
                                    </tr>
                                    <tr>
                                        <th>Total Steps / Goal</th>
                                        <td>{body_stats_data['Total Steps / Goal']}</td>
                                    </tr>
                                    <tr>
                                        <th>Distance</th>
                                        <td>{body_stats_data['Distance']}</td>
                                    </tr>
                                    <tr>
                                        <th>Highly Active Duration</th>
                                        <td>{body_stats_data['Highly Active Duration']}</td>
                                    </tr>
                                    <tr>
                                        <th>Active Duration</th>
                                        <td>{body_stats_data['Active Duration']}</td>
                                    </tr>
                                    <tr>
                                        <th>Sedentary Duration</th>
                                        <td>{body_stats_data['Sedentary Duration']}</td>
                                    </tr>
                                    <tr>
                                        <th>Moderate Intensity Minutes</th>
                                        <td>{body_stats_data['Moderate Intensity Minutes']}</td>
                                    </tr>
                                    <tr>
                                        <th>Vigorous Intensity Minutes</th>
                                        <td>{body_stats_data['Vigorous Intensity Minutes']}</td>
                                    </tr>
                                    <tr>
                                        <th>Intensity Minutes Goal Status</th>
                                        <td>{body_stats_data['Intensity Minutes Goal Status']}</td>
                                    </tr>
                                    <tr>
                                        <th>Floors Up</th>
                                        <td>{body_stats_data['Floors Up']}</td>
                                    </tr>
                                    <tr>
                                        <th>Floors Down</th>
                                        <td>{body_stats_data['Floors Down']}</td>
                                    </tr>
                                    <tr>
                                        <th>Heart Rate - Min/Resting/Max</th>
                                        <td>{body_stats_data['Heart Rate - Min/Resting/Max']}</td>
                                    </tr>
                                    <tr>
                                        <th>Last Seven Days Avg Resting Heart Rate</th>
                                        <td>{body_stats_data['Last Seven Days Avg Resting Heart Rate']}</td>
                                    </tr>
                                    <tr>
                                        <th>Average Stress</th>
                                        <td>{body_stats_data['Average Stress']}</td>
                                    </tr>
                                    <tr>
                                        <th>Max Stress Level</th>
                                        <td>{body_stats_data['Max Stress Level']}</td>
                                    </tr>
                                    <tr>
                                        <th>Stress Duration</th>
                                        <td>{body_stats_data['Stress Duration']}</td>
                                    </tr>
                                    <tr>
                                        <th>Blood Oxygen (SpO2)</th>
                                        <td>{body_stats_data['Blood Oxygen (SpO2)']}</td>
                                    </tr>
                                </table>
                            </div>
                        </div>
                    </div>
                    <div class="footer">
                    <p>Have a great day!</p>
                    <img src="https://lh3.googleusercontent.com/pw/AP1GczMyn-jztxA6E7Va572D3c8r00tPo7PpT35tkpYqLez72sDBLXai3ZXQJEc9doLAWUGjdgkq4846yU1p3-vzDYMCvHIqYzfQ9OlONFhzeLW3DCzSggOW9RDXsntkNHvLe251U7CbQ4q2Lepast7mWo0=w808-h278-s-no" alt="Garmin Statistics" style="max-width:100px;width:100%;height:auto;margin-top:10px;">
                </div>

                </div>
            </body>
            </html>
            """
        except Exception as e:
            message = f"<p>No Data Available: {e}</p>"
            print(message)
        return message

    def formatStravaActivityText(self, activity_data):
        name = activity_data.get("name", "Unnamed Activity")
        distance = activity_data.get("distance", 0)
        moving_time = activity_data.get("moving_time", 0)
        start_date = activity_data.get("start_date_local", "")
        average_speed = activity_data.get("average_speed", 0)
        max_speed = activity_data.get("max_speed", 0)
        average_heartrate = activity_data.get("average_heartrate", 0)
        max_heartrate = activity_data.get("max_heartrate", 0)
        cadence = 2 * (activity_data.get("average_cadence", 0))

        formatted_start_date = datetime.datetime.strptime(
            start_date, "%Y-%m-%dT%H:%M:%SZ"
        ).strftime("%Y-%m-%d %H:%M:%S")

        message = (
            f"Activity: {name}\n"
            f"Distance: {distance / 1000:.2f} km\n"
            f"Moving Time: {CommonUtils().seconds_to_hm(moving_time)}\n"
            f"Start Date: {formatted_start_date}\n"
            f"Average Speed: {CommonUtils().convert_speed_mps_to_minkm(average_speed)}\n"
            f"Max Speed: {CommonUtils().convert_speed_mps_to_minkm(max_speed)}\n"
            f"Average Heartrate: {average_heartrate} BPM\n"
            f"Max Heartrate: {max_heartrate} BPM\n"
            f"Average Cadence: {cadence} SPM"
        )

        return message

    def formatStravaActivityHtml(self, activity_data):
        name = activity_data.get("name", "Unnamed Activity")
        distance = activity_data.get("distance", 0)
        moving_time = activity_data.get("moving_time", 0)
        start_date = activity_data.get("start_date_local", "")
        average_speed = activity_data.get("average_speed", 0)
        max_speed = activity_data.get("max_speed", 0)
        average_heartrate = activity_data.get("average_heartrate", 0)
        max_heartrate = activity_data.get("max_heartrate", 0)
        cadence = 2 * (activity_data.get("average_cadence", 0))

        formatted_start_date = datetime.datetime.strptime(
            start_date, "%Y-%m-%dT%H:%M:%SZ"
        ).strftime("%Y-%m-%d %H:%M:%S")

        message = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Strava Activity</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    width: 100%;
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: #fff;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    border-radius: 8px;
                    margin-top: 20px;
                }}
                .header {{
                    background-color: #0073e6;
                    color: white;
                    padding: 10px 20px;
                    text-align: center;
                    border-radius: 8px 8px 0 0;
                }}
                .content {{
                    padding: 20px;
                }}
                .section {{
                    margin-bottom: 30px;
                }}
                .section-title {{
                    font-size: 1.4em;
                    margin-bottom: 10px;
                    color: #0073e6;
                }}
                .stats {{
                    margin-bottom: 20px;
                    border-top: 1px solid #ddd;
                    padding-top: 10px;
                }}
                .stats p {{
                    margin: 5px 0;
                }}
                .footer {{
                    text-align: center;
                    color: #777;
                    font-size: 0.9em;
                    padding: 10px;
                    border-top: 1px solid #ddd;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Strava Activity</h1>
                </div>
                <div class="content">
                    <div class="section">
                        <h2 class="section-title">Activity Details</h2>
                        <div class="stats">
                            <p><strong>Name:</strong> {name}</p>
                            <p><strong>Distance:</strong> {distance / 1000:.2f} km</p>
                            <p><strong>Moving Time:</strong> {CommonUtils().seconds_to_hm(moving_time)}</p>
                            <p><strong>Start Date:</strong> {formatted_start_date}</p>
                            <p><strong>Average Speed:</strong> {CommonUtils().convert_speed_mps_to_minkm(average_speed)}</p>
                            <p><strong>Max Speed:</strong> {CommonUtils().convert_speed_mps_to_minkm(max_speed)}</p>
                            <p><strong>Average Heartrate:</strong> {average_heartrate} BPM</p>
                            <p><strong>Max Heartrate:</strong> {max_heartrate} BPM</p>
                            <p><strong>Average Cadence:</strong> {cadence} SPM</p>
                        </div>
                    </div>
                </div>
                <div class="footer">
                    <p>Have a great day!</p>
                </div>
            </div>
        </body>
        </html>
        """
        return message

    def formatStravaActivityHtml2(self, activity_data):
        name = activity_data.get("name", "Unnamed Activity")
        distance = activity_data.get("distance", 0)
        moving_time = activity_data.get("moving_time", 0)
        start_date = activity_data.get("start_date_local", "")
        average_speed = activity_data.get("average_speed", 0)
        max_speed = activity_data.get("max_speed", 0)
        average_heartrate = activity_data.get("average_heartrate", 0)
        max_heartrate = activity_data.get("max_heartrate", 0)
        cadence = 2 * (activity_data.get("average_cadence", 0))
        average_temp = activity_data.get("average_temp", 0)
        calories = activity_data.get("kilojoules", 0)
        formatted_start_date = datetime.strptime(
            start_date, "%Y-%m-%dT%H:%M:%SZ"
        ).strftime("%Y-%m-%d %H:%M:%S")
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Strava Activity Summary</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    padding: 20px;
                }}
                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: #ffffff;
                    border-radius: 10px;
                    overflow: hidden;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                }}
                .header {{
                    background-color: #007bff;
                    color: #ffffff;
                    padding: 10px;
                    text-align: center;
                    font-size: 24px;
                }}
                .content {{
                    padding: 20px;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-bottom: 20px;
                }}
                th, td {{
                    padding: 10px;
                    text-align: left;
                    border-bottom: 1px solid #ddd;
                }}
                th {{
                    background-color: #007bff;
                    color: #ffffff;
                }}
                .highlight {{
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                Strava Activity Summary<br>{datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ").strftime('%A, %d %b %Y')}
                </div>
                <div class="content">
                    <table>
                        <tr>
                            <th colspan="2">Activity Details</th>
                        </tr>
                        <tr>
                            <td class="highlight">Activity Name:</td>
                            <td>{name}</td>
                        </tr>
                        <tr>
                            <td class="highlight">Distance:</td>
                            <td>{distance / 1000:.2f} km</td>
                        </tr>
                        <tr>
                            <td class="highlight">Moving Time:</td>
                            <td>{CommonUtils().seconds_to_hm(moving_time)}</td>
                        </tr>
                        <tr>
                            <td class="highlight">Start Date:</td>
                            <td>{formatted_start_date}</td>
                        </tr>
                        <tr>
                            <td class="highlight">Average Speed:</td>
                            <td>{CommonUtils().convert_speed_mps_to_minkm(average_speed)}</td>
                        </tr>
                        <tr>
                            <td class="highlight">Max Speed:</td>
                            <td>{CommonUtils().convert_speed_mps_to_minkm(max_speed)}</td>
                        </tr>
                        <tr>
                            <td class="highlight">Average Heartrate:</td>
                            <td>{average_heartrate} BPM</td>
                        </tr>
                        <tr>
                            <td class="highlight">Max Heartrate:</td>
                            <td>{max_heartrate} BPM</td>
                        </tr>
                        <tr>
                            <td class="highlight">Average Cadence:</td>
                            <td>{cadence} SPM</td>
                        </tr>
                        <tr>
                            <td class="highlight">Average Temp:</td>
                            <td>{average_temp} °C</td>
                        </tr>
                        <tr>
                            <td class="highlight">Calories:</td>
                            <td>{calories}</td>
                        </tr>
                    </table>
                    <p style="text-align: center; color: #888888;">Have a nice day.</p>
                </div>
            </div>
        </body>
        </html>
        """

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
        html_content += f'<div class="weather-header">{CommonUtils().timestamp_to_date(data_list["dt"])}</div>\n'
        html_content += '<div class="weather-details">\n'
        html_content += f'<p class="summary">Summary: {data_list["summary"]}</p>\n'
        html_content += '<table>\n'
        html_content += '<tr><th>Sunrise</th><th>Sunset</th><th>Temp Day</th><th>Temp Night</th><th>Feels Like Day</th><th>Feels Like Night</th><th>Humidity</th><th>Wind</th><th>UV Index</th></tr>\n'
        html_content += f'<tr><td class="sunrise-sunset">{CommonUtils().timestamp_to_datetime(data_list["sunrise"])}</td>'
        html_content += f'<td class="sunrise-sunset">{CommonUtils().timestamp_to_datetime(data_list["sunset"])}</td>'
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
            html_content += f'<tr><td>{CommonUtils().timestamp_to_time(hour["dt"])}</td>'
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

