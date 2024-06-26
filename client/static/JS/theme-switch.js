!(function () {
  "use strict";
  const e = "theme",
    t = "auto",
    i = "dark",
    n = "light",
    o = [t, i, n],
    a = "(prefers-color-scheme: dark)",
    s = "themeToggle",
    d = [10, 0, 33, 0],
    m = [10, 0, 20, 1],
    r = [5, 1, 33, 1];
  class l extends HTMLElement {
    shadowRoot;
    static counter = 0;
    identifier = l.counter++;
    constructor() {
      super(),
        (this.shadowRoot = this.attachShadow({ mode: "open" })),
        (this.shadowRoot.innerHTML = (function (e, t, i, n) {
          return ` <button id="theme-switch"> <svg viewBox="0 0 24 24" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg"> <defs> <mask id="mask"> <rect width="100%" height="100%" fill="#fff"/> <circle id="eclipse" r="10" cx="${i}" cy="6"> <animate id="eclipse-anim-come" fill="freeze" attributeName="cx" to="20" dur="300ms" begin="indefinite" calcMode="spline" keyTimes="0; 1" keySplines="0.37, 0, 0.63, 1"/> <animate id="eclipse-anim-go" fill="freeze" attributeName="cx" to="33" dur="300ms" begin="indefinite" calcMode="spline" keyTimes="0; 1" keySplines="0.37, 0, 0.63, 1"/> </circle> <g id="letter" fill="none" stroke="#000" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="1 1" stroke-dashoffset="${n}"> <path pathLength="1" d="m 8,16.5 4,-9 4,9"/> <path pathLength="1" d="M 8,16.5 9,14.5 h 6"/> <animate id="letter-anim-show" fill="freeze" attributeName="stroke-dashoffset" to="0" dur="400ms" begin="indefinite" calcMode="spline" keyTimes="0; 1" keySplines=".67,.27,.55,.9"/> <animate id="letter-anim-hide" fill="freeze" attributeName="stroke-dashoffset" to="1" dur="15ms" begin="indefinite" calcMode="spline" keyTimes="0; 1" keySplines="0.37, 0, 0.63, 1"/> </g> </mask> </defs> <g id="visible-content" mask="url(#mask)"> <g id="rays" opacity="${t}" fill="none" stroke="#000" stroke-width="2" stroke-linecap="round"> <animate id="rays-anim-hide" fill="freeze" attributeName="opacity" to="0" dur="100ms" begin="indefinite" calcMode="spline" keyTimes="0; 1" keySplines="0.37, 0, 0.63, 1"/> <animate id="rays-anim-show" fill="freeze" attributeName="opacity" to="1" dur="300ms" begin="indefinite" calcMode="spline" keyTimes="0; 1" keySplines="0.37, 0, 0.63, 1"/> <animateTransform id="rays-anim-rotate" attributeName="transform" attributeType="XML" type="rotate" from="-25 12 12" to="0 12 12" dur="300ms" begin="indefinite" calcMode="spline" keyTimes="0; 1" keySplines="0.37, 0, 0.63, 1"/> <path d="m12 1v3"/> <path d="m23 12h-3"/> <path d="m19.778 4.2218-2.121 2.1213"/> <path d="m19.778 19.778-2.121-2.121"/> <path d="m4.222 19.778 2.121-2.121"/> <path d="m4.222 4.222 2.121 2.121"/> <path d="m4 12h-3"/> <path d="m12 20v3"/> </g> <circle id="circle" r="${e}" cx="12" cy="12"> <animate id="core-anim-enlarge" fill="freeze" attributeName="r" to="10" dur="300ms" begin="indefinite" calcMode="spline" keyTimes="0; 1" keySplines="0.37, 0, 0.63, 1"/> <animate id="core-anim-shrink" fill="freeze" attributeName="r" to="5" dur="300ms" begin="indefinite" calcMode="spline" keyTimes="0; 1" keySplines="0.37, 0, 0.63, 1"/> </circle> </g> </svg> </button> `;
        })(
          ...(function () {
            const e = c();
            return e === t ? d : e === i ? m : r;
          })()
        )),
        this.shadowRoot.host.addEventListener("click", this.onClick),
        document.addEventListener(s, (e) => {
          e.detail.originId !== this.identifier && this.adaptToTheme();
        }),
        window.addEventListener("storage", (t) => {
          t.key === e && (this.adaptToTheme(), h());
        });
      const n = document.createElement("style");
      (n.textContent =
        ":host{display:flex;width:var(--dummy-variable,24px);aspect-ratio:1/1;cursor:pointer}:host([hidden]){display:none}button{padding:0;border:none;background:0 0;display:flex;cursor:pointer}#circle{fill:var(--theme-switch-icon-color,#000)}#rays{stroke:var(--theme-switch-icon-color,#000)}"),
        this.shadowRoot.append(n);
    }
    onClick() {
      const e = c();
      this.toggleTheme(e);
      const t = c(),
        i = this.createEvent(e, t);
      this.dispatchEvent(i);
    }
    createEvent(e, t) {
      return new CustomEvent(s, {
        detail: { originId: this.identifier, oldState: e, newState: t },
        bubbles: !0,
        composed: !0,
        cancelable: !1,
      });
    }
    toggleTheme(o) {
      o === t
        ? (localStorage.setItem(e, n), this.animateThemeButtonIconToLight())
        : o === i
        ? (localStorage.setItem(e, t), this.animateThemeButtonIconToAuto())
        : (localStorage.setItem(e, i), this.animateThemeButtonIconToDark()),
        h();
    }
    adaptToTheme() {
      const e = c();
      e === t
        ? this.animateThemeButtonIconToAuto()
        : e === i
        ? this.animateThemeButtonIconToDark()
        : this.animateThemeButtonIconToLight();
    }
    animateThemeButtonIconToLight() {
      this.shadowRoot.getElementById("letter-anim-hide").beginElement(),
        this.shadowRoot.getElementById("core-anim-shrink").beginElement(),
        this.shadowRoot.getElementById("rays-anim-rotate").beginElement(),
        this.shadowRoot.getElementById("rays-anim-show").beginElement();
    }
    animateThemeButtonIconToAuto() {
      this.shadowRoot.getElementById("eclipse-anim-go").beginElement(),
        this.shadowRoot.getElementById("letter-anim-show").beginElement();
    }
    animateThemeButtonIconToDark() {
      this.shadowRoot.getElementById("rays-anim-hide").beginElement(),
        this.shadowRoot.getElementById("core-anim-enlarge").beginElement(),
        this.shadowRoot.getElementById("eclipse-anim-come").beginElement();
    }
  }
  function h() {
    let e = c();
    e === t && (e = window.matchMedia(a).matches ? i : n),
      document.documentElement.setAttribute("data-theme", e);
  }
  function c() {
    const t = localStorage.getItem(e);
    return o.includes(t) ? t : "auto";
  }
  h(),
    window.customElements.define("theme-switch", l),
    window.matchMedia(a).addEventListener("change", h);
})();
//# sourceMappingURL=theme-switch.min.js.map
