style_component = """<style>
          .header {
            font: 600 18px 'Segoe UI', Ubuntu, Sans-Serif;
            fill: #Header_Color;
            animation: fadeInAnimation 0.8s ease-in-out forwards;
          }
          @supports(-moz-appearance: auto) {
            /* Selector detects Firefox */
            .header { font-size: 15.5px; }
          }
          
    .stat {
      font: 600 14px 'Segoe UI', Ubuntu, "Helvetica Neue", Sans-Serif; fill: #ffffff;
    }
    @supports(-moz-appearance: auto) {
      /* Selector detects Firefox */
      .stat { font-size:FONT_SIZE; }
    }
    .stagger {
      opacity: 0;
      animation: fadeInAnimation 0.3s ease-in-out forwards;
    }
    .rank-text {
      font: 800 24px 'Segoe UI', Ubuntu, Sans-Serif; fill: #ffffff;
      animation: scaleInAnimation 0.3s ease-in-out forwards;
    }
    .rank-percentile-header {
      font-size: 14px;
    }
    .rank-percentile-text {
      font-size: 16px;
    }
    
    .not_bold { font-weight: 400 }
    .bold { font-weight: 700 }
    .icon {
      fill: #Header_Color;
      display: block;
    }

    .rank-circle-rim {
      stroke: #57bcda;
      fill: none;
      stroke-width: 6;
      opacity: 0.2;
    }
    .rank-circle {
      stroke: #57bcda;
      stroke-dasharray: 250;
      fill: none;
      stroke-width: 6;
      stroke-linecap: round;
      opacity: 0.8;
      transform-origin: -10px 8px;
      transform: rotate(-90deg);
      animation: rankAnimation 1s forwards ease-in-out;
    }
    
    @keyframes rankAnimation {
      from {
        stroke-dashoffset: 251.32741228718345;
      }
      to {
        stroke-dashoffset: 151.99434128748638;
      }
    }
  
  

          
      /* Animations */
      @keyframes scaleInAnimation {
        from {
          transform: translate(-5px, 5px) scale(0);
        }
        to {
          transform: translate(-5px, 5px) scale(1);
        }
      }
      @keyframes fadeInAnimation {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }
    
          
        </style>"""



from .icon_svg import *

line_component = f"""

    <g class="stagger" style="animation-delay: 450ms" transform="translate(25, 0)">
      
    <svg data-testid="icon" class="icon" viewBox="0 0 24 24" version="1.1" width="16" height="16">
     icon_svg_sample
    </svg>
    LINE_HERE
    </g>
  </g><g transform="translate(0, Ylocation)">

"""


circle_chart_component = """
    <g data-testid="rank-circle"
          transform="translate(450.5, 47.5)">
        <circle class="rank-circle-rim" cx="-10" cy="8" r="40" />
        <circle class="rank-circle" cx="-10" cy="8" r="40" />
        <g class="rank-text">
          
        <text x="-5" y="3" alignment-baseline="central" dominant-baseline="central" text-anchor="middle" data-testid="level-rank-icon">
          T
        </text>
      
        </g>
      </g>
"""

pizza_icon_component = f"""
    <g 
          transform="translate(420.5, 10)">
        <g class="rank-text">
          
          <svg data-testid="icon" class="icon" viewBox="0 0 24 24" version="1.1" width="64" height="64">
            {PIZZA}
          </svg>

        </g>
      </g>
"""

sample = f"""


      <svg
        width="width_custom"
        height="height_sutom"
        viewBox="0 0 width_custom height_sutom"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        role="img"
        aria-labelledby="descId"
      >
        <title id="titleId">Username's GitHub Information</title>
        <desc id="descId">Profile pizza for Username </desc>
        {style_component}

        

        <rect
          data-testid="card-bg"
          x="0.5"
          y="0.5"
          rx="4.5"
          height="99%"
          stroke="#e4e2e2"
          width="width_custom2"
          fill="#bgcolor"
          stroke-opacity="0"
        />

        
      <g
        data-testid="card-title"
        transform="translate(25, 35)"
      >
        <g transform="translate(0, 0)">
      <text
        x="0"
        y="0"
        class="header"
        data-testid="header"
      >USERNAME_'s Profile Pizza</text>
    </g>
      </g>
    

        <g
          data-testid="main-card-body"
          transform="translate(0, 55)"
        >

        {pizza_icon_component}
          

    <svg x="0" y="0">
      <g transform="translate(0, 0)">

      


    LINE_COMPONENTS


  </g>
    </svg>
  
        </g>
      </svg>
    


"""