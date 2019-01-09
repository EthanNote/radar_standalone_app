import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)
Vue.prototype.user = [
  {
    'name': 'ichuangtu',
    'level': 'admin',
    'createdDate': '2005-11-01',
    'email': 'f.qmcolkgq@mzfqpxvw.sd'
  },
  {
    'name': 'TNqo',
    'level': 'user',
    'createdDate': '1982-12-02',
    'email': 'i.ltrt@lhvl.gn'
  },
  {
    'name': 'O%LOb',
    'level': 'user',
    'createdDate': '1994-10-25',
    'email': 'u.oqvp@gzwdwg.fk'
  },
  {
    'name': 'w0jU',
    'level': 'user',
    'createdDate': '2015-11-08',
    'email': 'e.skxmpgy@hnllvmpbr.gm'
  }
]
export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'landing-page',
    //   component: require('@/components/LandingPage').default
    // },
    // {
    //   path: '/',
    //   name: 'radar-monitor',
    //   component: require('@/components/RadarMonitor').default
    // },

    {
      path: '/',
      name: 'home',
      component: require('@/components/Home').default
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
