This will be a guide for 'ModuleScript' usage. We will cover the basics of the Roblox engine APIs and some functions + formating.

-- || how to get the module || --
-- || Services || --
local RepS = game:GetService("ReplicatedStorage")
-- || Data || --
local Module = require(RepS.module)
-- || Functions || --
for i,v in pairs(Module) do
    print(i,v) -- "i","v" can be anything 
end

