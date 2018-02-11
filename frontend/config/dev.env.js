'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  consumer_key: '"B4vSFikLR3fUf6yavsATgEn9Y"',
  consumer_secret: '"LtulxuF9ew3PzY9bpkEdmU28xZm3XNMYev8Lit2ADBv3GREDI3"',
  access_token_key: '"246248425-Tlzgqm3gKduShh0C5bwpvBuHHPimD15rdrsxnTge"',
  access_token_secret: '""'
})
