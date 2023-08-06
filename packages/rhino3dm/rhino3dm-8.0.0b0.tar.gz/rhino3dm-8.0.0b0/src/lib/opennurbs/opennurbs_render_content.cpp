//
// Copyright (c) 1993-2022 Robert McNeel & Associates. All rights reserved.
// OpenNURBS, Rhinoceros, and Rhino3D are registered trademarks of Robert
// McNeel & Associates.
//
// THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT EXPRESS OR IMPLIED WARRANTY.
// ALL IMPLIED WARRANTIES OF FITNESS FOR ANY PARTICULAR PURPOSE AND OF
// MERCHANTABILITY ARE HEREBY DISCLAIMED.
//
// For complete openNURBS copyright information see <http://www.opennurbs.org>.
//
////////////////////////////////////////////////////////////////

#include "opennurbs.h"
#include "opennurbs_internal_defines.h"

#if !defined(ON_COMPILING_OPENNURBS)
// This check is included in all opennurbs source .c and .cpp files to insure
// ON_COMPILING_OPENNURBS is defined when opennurbs source is compiled.
// When opennurbs source is being compiled, ON_COMPILING_OPENNURBS is defined
// and the opennurbs .h files alter what is declared and how it is declared.
#error ON_COMPILING_OPENNURBS must be defined when compiling opennurbs
#endif

#define ON_TYPE_NAME               L"type-name"
#define ON_TYPE_ID                 L"type-id"
#define ON_INSTANCE_ID             L"instance-id"
#define ON_RENDER_ENGINE_ID        L"render-engine-id"
#define ON_PLUG_IN_ID              L"plug-in-id"
#define ON_GROUP_ID                L"group-id"
#define ON_INSTANCE_NAME           L"instance-name"
#define ON_CHILD_SLOT_NAME         L"child-slot-name"
#define ON_NOTES                   L"notes"
#define ON_TAGS                    L"tags"
#define ON_HIDDEN                  L"hidden"
#define ON_REFERENCE               L"reference"
#define ON_AUTO_DELETE             L"auto-delete"
#define ON_ENV_BACKGROUND_COLOR    L"background-color"
#define ON_POSTFIX_SECTION         L"-section"
#define ON_PARAMETERS              L"parameters"
#define ON_PARAMETERS_V8           L"parameters-v8"
#define ON_SIMULATION              L"simulation"

#define ON_POSTFIX_SECTION         L"-section"
#define ON_PARAMETERS              L"parameters"
#define ON_PARAMETERS_V8           L"parameters-v8"
#define ON_SIMULATION              L"simulation"

#define ON_ENV_PROJ_BOX            L"box"
#define ON_ENV_PROJ_CUBE_MAP       L"cubemap"
#define ON_ENV_PROJ_CUBE_MAP_HORZ  L"horizontal-cross-cubemap"
#define ON_ENV_PROJ_CUBE_MAP_VERT  L"vertical-cross-cubemap"
#define ON_ENV_PROJ_EMAP           L"emap"
#define ON_ENV_PROJ_HEMISPHERICAL  L"hemispherical"
#define ON_ENV_PROJ_LIGHT_PROBE    L"lightprobe"
#define ON_ENV_PROJ_PLANAR         L"planar"
#define ON_ENV_PROJ_SPHERICAL      L"spherical"

// General parameters used by materials that simulate ON_Material.
//
// These are copied from the FS_ strings in the RDK. Perhaps the RDK should start
// using these instead of the FS_ ones. Or the FS_ ones can be defined as these.
// Remember, they are in the RDK SDK. Check with Andy.

#define ON_MAT_ALPHA_TRANSPARENCY                 L"alpha-transparency"
#define ON_MAT_AMBIENT                            L"ambient"
#define ON_MAT_DIFFUSE                            L"diffuse"
#define ON_MAT_DISABLE_LIGHTING                   L"disable-lighting"
#define ON_MAT_EMISSION                           L"emission"
#define ON_MAT_FLAMINGO_LIBRARY                   L"flamingo-library"
#define ON_MAT_FRESNEL_ENABLED                    L"fresnel-enabled"
#define ON_MAT_CLARITY_AMOUNT                     L"clarity-amount"
#define ON_MAT_IOR                                L"ior"
#define ON_MAT_POLISH_AMOUNT                      L"polish-amount"
#define ON_MAT_SHINE                              L"shine"      // Value is 0.0..1.0, NOT ON_Material::MaxShine.
#define ON_MAT_SPECULAR                           L"specular"
#define ON_MAT_REFLECTIVITY_AMOUNT                L"reflectivity"
#define ON_MAT_REFLECTION                         L"reflection" // Simulation is different to Custom Material.
#define ON_MAT_TRANSPARENCY_AMOUNT                L"transparency"
#define ON_MAT_TRANSPARENT                        L"transparent" // Simulation is different to Custom Material.
#define ON_MAT_IS_PHYSICALLY_BASED                L"is-physically-based"

#define ON_MAT_POSTFIX_ON                         L"on"
#define ON_MAT_POSTFIX_AMOUNT                     L"amount"
#define ON_MAT_POSTFIX_FILTER_ON                  L"filter-on"

#define ON_MAT_BITMAP_TEXTURE                     L"bitmap-texture"
#define ON_MAT_BUMP_TEXTURE                       L"bump-texture"
#define ON_MAT_TRANSPARENCY_TEXTURE               L"transparency-texture"
#define ON_MAT_ENVIRONMENT_TEXTURE                L"environment-texture"

#define ON_MAT_PBR_BRDF                           L"pbr-brdf"
#define   ON_MAT_PBR_BRDF_GGX                       L"ggx"
#define   ON_MAT_PBR_BRDF_WARD                      L"ward"
#define ON_MAT_PBR_ALPHA                          L"pbr-alpha"
#define ON_MAT_PBR_ANISOTROPIC                    L"pbr-anisotropic"
#define ON_MAT_PBR_ANISOTROPIC_ROTATION           L"pbr-anisotropic-rotation"
#define ON_MAT_PBR_BASE_COLOR                     L"pbr-base-color"
#define ON_MAT_PBR_CLEARCOAT                      L"pbr-clearcoat"
#define ON_MAT_PBR_CLEARCOAT_ROUGHNESS            L"pbr-clearcoat-roughness"
#define ON_MAT_PBR_EMISSION_COLOR                 L"pbr-emission"
#define ON_MAT_PBR_METALLIC                       L"pbr-metallic"
#define ON_MAT_PBR_OPACITY                        L"pbr-opacity"
#define ON_MAT_PBR_OPACITY_IOR                    L"pbr-opacity-ior"
#define ON_MAT_PBR_OPACITY_ROUGHNESS              L"pbr-opacity-roughness"
#define ON_MAT_PBR_ROUGHNESS                      L"pbr-roughness"
#define ON_MAT_PBR_SHEEN                          L"pbr-sheen"
#define ON_MAT_PBR_SHEEN_TINT                     L"pbr-sheen-tint"
#define ON_MAT_PBR_SPECULAR                       L"pbr-specular"
#define ON_MAT_PBR_SPECULAR_TINT                  L"pbr-specular-tint"
#define ON_MAT_PBR_SUBSURFACE                     L"pbr-subsurface"
#define ON_MAT_PBR_SUBSURFACE_SCATTERING_COLOR    L"pbr-subsurface-scattering-color"
#define ON_MAT_PBR_SUBSURFACE_SCATTERING_RADIUS   L"pbr-subsurface-scattering-radius"
#define ON_MAT_PBR_USE_BASE_COLOR_TEXTURE_ALPHA   L"pbr-use-base-color-texture-alpha"

#define ON_TEX_FILENAME                    L"filename"

// Material's texture simulation (check with Andy what the heck this is even for).
#define ON_MAT_TEXSIM_FORMAT               L"Texture-%u-"
#define ON_MAT_TEXSIM_FILENAME             L"filename"
#define ON_MAT_TEXSIM_ON                   L"on"
#define ON_MAT_TEXSIM_AMOUNT               L"amount"
#define ON_MAT_TEXSIM_TYPE                 L"type"
#define ON_MAT_TEXSIM_FILTER               L"filter"
#define ON_MAT_TEXSIM_MODE                 L"mode"
#define ON_MAT_TEXSIM_UVW                  L"uvw"
#define ON_MAT_TEXSIM_WRAP_U               L"wrap-u"
#define ON_MAT_TEXSIM_WRAP_V               L"wrap-v"

// Environment simulation.
#define ON_ENVSIM_BACKGROUND_COLOR         L"background-color"
#define ON_ENVSIM_BACKGROUND_IMAGE         L"background-image"
#define ON_ENVSIM_BACKGROUND_PROJECTION    L"background-projection"

// Texture simulation.
#define ON_TEXSIM_FILENAME                 L"filename"
#define ON_TEXSIM_REPEAT                   L"repeat"
#define ON_TEXSIM_OFFSET                   L"offset"
#define ON_TEXSIM_ROTATION                 L"rotation"
#define ON_TEXSIM_WRAP_TYPE                L"wrap-type"
#define ON_TEXSIM_MAPPING_CHANNEL          L"mapping-channel"
#define ON_TEXSIM_PROJECTION_MODE          L"projection-mode" // Still have to write this out.

static void ON_ConstructXform(double scale_x, double scale_y, double scale_z,
                              double angle_x, double angle_y, double angle_z,
                              double trans_x, double trans_y, double trans_z, ON_Xform& xform)
{
  // All angles in degrees.

  const ON_Xform S = ON_Xform::DiagonalTransformation(scale_x, scale_y, scale_z);

  ON_Xform R;
  R.Rotation(ON_RadiansFromDegrees(angle_x), ON_3dVector::XAxis, ON_3dPoint::Origin);

  auto vRotate = ON_3dVector::YAxis;
  vRotate.Transform(R.Inverse());

  ON_Xform Ry;
  Ry.Rotation(ON_RadiansFromDegrees(angle_y), vRotate, ON_3dPoint::Origin);

  R = R * Ry;

  vRotate = ON_3dVector::ZAxis;
  vRotate.Transform(R.Inverse());

  ON_Xform Rz;
  Rz.Rotation(ON_RadiansFromDegrees(angle_z), vRotate, ON_3dPoint::Origin);

  R = R * Rz;

  const auto T = ON_Xform::TranslationTransformation(-trans_x, -trans_y, -trans_z);

  xform = S * R * T;
}

static void ON_DeconstructXform(const ON_Xform& xformIn,
                                double& scale_x, double& scale_y, double& scale_z,
                                double& angle_x, double& angle_y, double& angle_z,
                                double& trans_x, double& trans_y, double& trans_z)
{
  // Returns all angles in degrees.

  ON_Xform xform = xformIn;

  scale_x = sqrt(xform[0][0] * xform[0][0] + xform[0][1] * xform[0][1] + xform[0][2] * xform[0][2]);
  scale_y = sqrt(xform[1][0] * xform[1][0] + xform[1][1] * xform[1][1] + xform[1][2] * xform[1][2]);
  scale_z = sqrt(xform[2][0] * xform[2][0] + xform[2][1] * xform[2][1] + xform[2][2] * xform[2][2]);

  ON_Xform S;
  ON_ConstructXform(scale_x, scale_y, scale_z, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, S);
  S.Invert();

  xform = S * xform;

  const double dSinBeta = -xform[2][0];

  double dCosBeta = sqrt(1.0 - dSinBeta * dSinBeta);
  if (dCosBeta < 0.0)
  {
    dCosBeta = -dCosBeta;
  }

  double dSinAlpha, dCosAlpha, dSinGamma, dCosGamma;

  if (dCosBeta < 1e-6)
  {
    dSinAlpha = -xform[1][2];
    dCosAlpha = xform[1][1];
    dSinGamma = 0.0;
    dCosGamma = 1.0;
  }
  else
  {
    dSinAlpha = xform[2][1] / dCosBeta;
    dCosAlpha = xform[2][2] / dCosBeta;
    dSinGamma = xform[1][0] / dCosBeta;
    dCosGamma = xform[0][0] / dCosBeta;
  }

  angle_x = (ON_DegreesFromRadians(atan2(dSinAlpha, dCosAlpha)));
  angle_y = (ON_DegreesFromRadians(atan2(dSinBeta, dCosBeta)));
  angle_z = (ON_DegreesFromRadians(atan2(dSinGamma, dCosGamma)));

  ON_Xform R;
  ON_ConstructXform(scale_x, scale_y, scale_z, angle_x, angle_y, angle_z, 0.0, 0.0, 0.0, R);
  R.Invert();

  ON_Xform T = R * xformIn;

  trans_x = -T[0][3];
  trans_y = -T[1][3];
  trans_z = -T[2][3];
}

struct XF
{
  double scale_x = 0.0, scale_y = 0.0, scale_z = 0.0;
  double angle_x = 0.0, angle_y = 0.0, angle_z = 0.0;
  double trans_x = 0.0, trans_y = 0.0, trans_z = 0.0;
};

static void ON_DeconstructXform(const ON_Xform& xform, XF& xf)
{
  ON_DeconstructXform(xform, xf.scale_x, xf.scale_y, xf.scale_z, xf.angle_x, xf.angle_y, xf.angle_z, xf.trans_x, xf.trans_y, xf.trans_z);
}

static void ON_ConstructXform(const XF& xf, ON_Xform& xform)
{
  ON_ConstructXform(xf.scale_x, xf.scale_y, xf.scale_z, xf.angle_x, xf.angle_y, xf.angle_z, xf.trans_x, xf.trans_y, xf.trans_z, xform);
}

ON_OBJECT_IMPLEMENT(ON_Environment, ON_Object, "94BCA4D5-0FC7-435E-95F9-22F3927F9B2E");

class ON_Environment::CImpl
{
public:
  CImpl();
  CImpl(const CImpl& src);

public:
  ON_Color m_back_col;
  ON_Texture m_back_image;
  BackgroundProjections m_back_proj = BackgroundProjections::Planar;
};

ON_Environment::CImpl::CImpl()
  :
  m_back_col(ON_Color(160, 160, 160))
{
}

ON_Environment::CImpl::CImpl(const CImpl& src)
{
  m_back_col   = src.m_back_col;
  m_back_proj  = src.m_back_proj;
  m_back_image = src.m_back_image;
}

ON_Environment::ON_Environment()
{
  m_impl = new CImpl;
}

ON_Environment::ON_Environment(const ON_Environment& src)
{
  m_impl = new CImpl(*src.m_impl);
}

ON_Environment::~ON_Environment()
{
  delete m_impl;
  m_impl = nullptr;
}

static ON__UINT32 CRCOnlyRGB(ON__UINT32 current_remainder, const ON_Color& c)
{
  const auto x = (unsigned int)c & 0x00FFFFFF;
  return ON_CRC32(current_remainder, sizeof(x), &x);
}

ON__UINT32 ON_Texture_CRC(const ON_Texture& tex)
{
  ON_wString file(tex.m_image_file_reference.FullPath());
#ifdef ON_RUNTIME_WIN
  file.MakeLower();
#endif
  ON__UINT32 crc = file.DataCRC(0);

  crc = ON_CRC32(crc, sizeof(tex.m_mapping_channel_id), &tex.m_mapping_channel_id);

  crc = ON_CRC32(crc, sizeof(tex.m_bOn),       &tex.m_bOn);
  crc = ON_CRC32(crc, sizeof(tex.m_type),      &tex.m_type);
  crc = ON_CRC32(crc, sizeof(tex.m_minfilter), &tex.m_minfilter);
  crc = ON_CRC32(crc, sizeof(tex.m_magfilter), &tex.m_magfilter);
  crc = ON_CRC32(crc, sizeof(tex.m_wrapu),     &tex.m_wrapu);
  crc = ON_CRC32(crc, sizeof(tex.m_wrapv),     &tex.m_wrapv);
  crc = ON_CRC32(crc, sizeof(tex.m_wrapw),     &tex.m_wrapw);

  crc = CRCOnlyRGB(crc, tex.m_border_color);
  crc = CRCOnlyRGB(crc, tex.m_transparent_color);
  crc = CRCOnlyRGB(crc, tex.m_blend_constant_RGB);

  crc = ON_CRC32(crc, sizeof(tex.m_blend_order), &tex.m_blend_order);

  const double amount = int(tex.m_blend_constant_A * 100.0) / 100.0;
  crc = ON_CRC32(crc, sizeof(amount), &amount);

  crc = ON_CRC32(crc, sizeof(tex.m_bump_scale), &tex.m_bump_scale);
  crc = ON_CRC32(crc, sizeof(tex.m_uvw),        &tex.m_uvw);

  crc = ON_CRC32(crc, sizeof(tex.m_blend_A0),   &tex.m_blend_A0);
  crc = ON_CRC32(crc, sizeof(tex.m_blend_RGB0), &tex.m_blend_RGB0);
  crc = ON_CRC32(crc, sizeof(tex.m_blend_A1),   &tex.m_blend_A1);
  crc = ON_CRC32(crc, sizeof(tex.m_blend_RGB1), &tex.m_blend_RGB1);
  crc = ON_CRC32(crc, sizeof(tex.m_blend_A2),   &tex.m_blend_A2);
  crc = ON_CRC32(crc, sizeof(tex.m_blend_RGB2), &tex.m_blend_RGB2);
  crc = ON_CRC32(crc, sizeof(tex.m_blend_A3),   &tex.m_blend_A3);
  crc = ON_CRC32(crc, sizeof(tex.m_blend_RGB3), &tex.m_blend_RGB3);

  crc = ON_CRC32(crc, sizeof(tex.m_bTreatAsLinear), &tex.m_bTreatAsLinear);

	return crc;
}

bool ON_Environment::operator == (const ON_Environment& env) const
{
  if (m_impl->m_back_col < env.m_impl->m_back_col)
    return false;

  if (m_impl->m_back_col > env.m_impl->m_back_col)
    return false;

  if (m_impl->m_back_proj != env.m_impl->m_back_proj)
    return false;

  if (ON_Texture_CRC(m_impl->m_back_image) != ON_Texture_CRC(env.m_impl->m_back_image))
    return false;

  return true;
}

bool ON_Environment::operator != (const ON_Environment& env) const
{
  return !(operator == (env));
}

const ON_Environment& ON_Environment::operator = (const ON_Environment& src)
{
  if (this != &src)
  {
    delete m_impl;
    m_impl = new CImpl(*src.m_impl);
  }

  return *this;
}

ON_Color ON_Environment::BackgroundColor(void) const
{
  return m_impl->m_back_col;
}

void ON_Environment::SetBackgroundColor(ON_Color color)
{
  m_impl->m_back_col = color;
}

ON_Texture ON_Environment::BackgroundImage(void) const
{
  return m_impl->m_back_image;
}

void ON_Environment::SetBackgroundImage(const ON_Texture& tex)
{
  m_impl->m_back_image = tex;
}

ON_Environment::BackgroundProjections ON_Environment::BackgroundProjection(void) const
{
  return m_impl->m_back_proj;
}

void ON_Environment::SetBackgroundProjection(ON_Environment::BackgroundProjections proj)
{
  m_impl->m_back_proj = proj;
}

ON_Environment::BackgroundProjections ON_Environment::ProjectionFromString(const wchar_t* wsz) // Static.
{
  if (0 == on_wcsicmp(ON_ENV_PROJ_PLANAR, wsz))        return BackgroundProjections::Planar;
  if (0 == on_wcsicmp(ON_ENV_PROJ_SPHERICAL, wsz))     return BackgroundProjections::Spherical;
  if (0 == on_wcsicmp(ON_ENV_PROJ_EMAP, wsz))          return BackgroundProjections::Emap;
  if (0 == on_wcsicmp(ON_ENV_PROJ_BOX, wsz))           return BackgroundProjections::Box;
  if (0 == on_wcsicmp(ON_ENV_PROJ_LIGHT_PROBE, wsz))   return BackgroundProjections::LightProbe;
  if (0 == on_wcsicmp(ON_ENV_PROJ_CUBE_MAP, wsz))      return BackgroundProjections::CubeMap;
  if (0 == on_wcsicmp(ON_ENV_PROJ_CUBE_MAP_VERT, wsz)) return BackgroundProjections::VerticalCrossCubeMap;
  if (0 == on_wcsicmp(ON_ENV_PROJ_CUBE_MAP_HORZ, wsz)) return BackgroundProjections::HorizontalCrossCubeMap;
  if (0 == on_wcsicmp(ON_ENV_PROJ_HEMISPHERICAL, wsz)) return BackgroundProjections::Hemispherical;

  ON_ASSERT(false);
  return BackgroundProjections::Planar;
}

const wchar_t* ON_Environment::StringFromProjection(BackgroundProjections proj) // Static.
{
  switch (proj)
  {
  case BackgroundProjections::Planar:                 return ON_ENV_PROJ_PLANAR;
  case BackgroundProjections::Spherical:              return ON_ENV_PROJ_SPHERICAL;
  case BackgroundProjections::Emap:                   return ON_ENV_PROJ_EMAP;
  case BackgroundProjections::Box:                    return ON_ENV_PROJ_BOX;
  case BackgroundProjections::LightProbe:             return ON_ENV_PROJ_LIGHT_PROBE;
  case BackgroundProjections::CubeMap:                return ON_ENV_PROJ_CUBE_MAP;
  case BackgroundProjections::VerticalCrossCubeMap:   return ON_ENV_PROJ_CUBE_MAP_VERT;
  case BackgroundProjections::HorizontalCrossCubeMap: return ON_ENV_PROJ_CUBE_MAP_HORZ;
  case BackgroundProjections::Hemispherical:          return ON_ENV_PROJ_HEMISPHERICAL;
  default: break;
  }

  ON_ASSERT(false);
  return ON_ENV_PROJ_PLANAR;
}

void* ON_Environment::EVF(const wchar_t* wszFunc, void* pvData)
{
  return nullptr;
}

ON_UUID RdkPlugInId(void)
{
  static ON_UUID uuid = { 0x16592D58, 0x4A2F, 0x401D, { 0xBF, 0x5E, 0x3B, 0x87, 0x74, 0x1C, 0x1B, 0x1B } };
  return uuid;
}

ON_UUID UniversalRenderEngineId(void)
{
  static ON_UUID uuid = { 0x99999999, 0x9999, 0x9999, { 0x99, 0x99, 0x99, 0x99, 0x99, 0x99, 0x99, 0x99 } };
  return uuid;
}

class ON_RenderContent::CImpl
{
public:
  CImpl(ON_RenderContent& rc, const wchar_t* kind);
  virtual ~CImpl();

  void SetXMLNode(const ON_XMLNode& node);

  const ON_XMLNode* XMLNode_Simulation(void) const;

  ON_RenderContent& TopLevel(void);

  bool AddChild(ON_RenderContent& rc);
  void DeleteAllChildren(void);

  ON_XMLVariant GetPropertyValue(const wchar_t* name) const;
  void SetPropertyValue(const wchar_t* name, const ON_XMLVariant& value);

  ON_RenderContent* FindChild(const wchar_t* child_slot_name) const;
  bool SetChild(ON_RenderContent* child, const wchar_t* child_slot_name);
  bool ChangeChild(ON_RenderContent* old_child, ON_RenderContent* new_child);

public:
  void InternalSetPropertyValue(const wchar_t* name, const ON_XMLVariant& value);

private:
  ON_RenderContent* FindLastChild(void) const;
  ON_RenderContent* FindPrevSibling(ON_RenderContent* child) const;

public:
  ONX_Model* m_model = nullptr;
  ON_XMLNode m_node;
  ON_RenderContent& m_render_content;
  ON_RenderContent* m_parent = nullptr;
  ON_RenderContent* m_first_child = nullptr;
  ON_RenderContent* m_next_sibling = nullptr;
  mutable std::recursive_mutex m_mutex;
};

ON_RenderContent::CImpl::CImpl(ON_RenderContent& rc, const wchar_t* kind)
  :
  m_node(kind),
  m_render_content(rc)
{
}

ON_RenderContent::CImpl::~CImpl()
{
  DeleteAllChildren();
}

const ON_XMLNode* ON_RenderContent::CImpl::XMLNode_Simulation(void) const
{
  return m_node.GetNamedChild(ON_SIMULATION);
}

ON_XMLVariant ON_RenderContent::CImpl::GetPropertyValue(const wchar_t* name) const
{
  // Gets a property from the content node. This is one of:
  //
  // - the material node <material... >
  // - the environment node <environment... >
  // - the texture node <texture... >

  std::lock_guard<std::recursive_mutex> lg(m_mutex);

  ON_XMLVariant v;

  const ON_XMLProperty* pProp = m_node.GetNamedProperty(name);
  if (nullptr != pProp)
  {
    v = pProp->GetValue();
  }

  return v;
}

void ON_RenderContent::CImpl::SetPropertyValue(const wchar_t* name, const ON_XMLVariant& value)
{
  std::lock_guard<std::recursive_mutex> lg(m_mutex);

  InternalSetPropertyValue(name, value);
}

void ON_RenderContent::CImpl::InternalSetPropertyValue(const wchar_t* name, const ON_XMLVariant& value)
{
  // Sets a property on the content node. This is one of:
  //
  // - the material node <material... >
  // - the environment node <environment... >
  // - the texture node <texture... >

  ON_XMLProperty* pProp = m_node.GetNamedProperty(name);
  if (nullptr != pProp)
  {
    pProp->SetValue(value);
  }
  else
  {
    pProp = m_node.AttachProperty(new ON_XMLProperty(name, value));
  }
}

void ON_RenderContent::CImpl::SetXMLNode(const ON_XMLNode& node)
{
  std::lock_guard<std::recursive_mutex> lg(m_mutex);

  // Copy the incoming XML node. The render content will only store a copy of its own XML, so
  // we will have to prune this copy as we find children and create render content children
  // for all the XML children.
  ON_XMLNode node_copy = node;

  // Iterate over the child nodes of the XML node being set to this content.
  auto it = node_copy.GetChildIterator();
  ON_XMLNode* child_node = nullptr;
  while (nullptr != (child_node = it.GetNextChild()))
  {
    // See if the child node is a content node.
    const ON_wString& name = child_node->TagName();
    if ((ON_KIND_MATERIAL == name) || (ON_KIND_ENVIRONMENT == name) || (ON_KIND_TEXTURE == name))
    {
      // Yes, so we are going to add a new render content to this hierarchy (recursively)
      // and remove this child node from the copy of the XML node.
      ON_RenderContent* child_rc = NewRenderContentFromNode(*child_node);
      if (nullptr != child_rc)
      {
        // Add the new content as a child of this content.
        AddChild(*child_rc);
      }

      delete node_copy.DetachChild(*child_node);
    }
  }

  // Copy the pruned copy of the XML node. This node does not have any child content nodes.
  m_node = node_copy;

  // Copy the XML instance name to the component name.
  m_render_content.SetName(GetPropertyValue(ON_INSTANCE_NAME).AsString());

  // Copy the XML instance id to the component id.
  m_render_content.SetId(GetPropertyValue(ON_INSTANCE_ID).AsUuid());
}

bool ON_RenderContent::CImpl::AddChild(ON_RenderContent& child)
{
  if ((nullptr != child.m_impl->m_model) || (nullptr != child.m_impl->m_parent) || (nullptr != child.m_impl->m_next_sibling))
    return false;

  if (nullptr == m_first_child)
  {
    m_first_child = &child;
  }
  else
  {
    ON_RenderContent* last_child = FindLastChild();
    if (nullptr == last_child)
      return false;

    last_child->m_impl->m_next_sibling = &child;
  }

  child.m_impl->m_next_sibling = nullptr;
  child.m_impl->m_parent = &m_render_content;

  return true;
}

void ON_RenderContent::CImpl::DeleteAllChildren(void)
{
  std::lock_guard<std::recursive_mutex> lg(m_mutex);

  if (nullptr == m_first_child)
    return;

  ON_RenderContent* child_rc = m_first_child;
  while (nullptr != child_rc)
  {
    auto* delete_rc = child_rc;
    child_rc = child_rc->m_impl->m_next_sibling;
    delete delete_rc;
  }

  m_first_child = nullptr;
}

ON_RenderContent* ON_RenderContent::CImpl::FindLastChild(void) const
{
  ON_RenderContent* result = nullptr;

  ON_RenderContent* candidate = m_first_child;
  while (nullptr != candidate)
  {
    result = candidate;
    candidate = candidate->m_impl->m_next_sibling;
  }

  return result;
}

ON_RenderContent* ON_RenderContent::CImpl::FindPrevSibling(ON_RenderContent* child) const
{
  if (child != m_first_child)
  {
    ON_RenderContent* candidate = m_first_child;
    while (nullptr != candidate)
    {
      if (child == candidate->m_impl->m_next_sibling)
        return candidate;

      candidate = candidate->m_impl->m_next_sibling;
    }
  }

  return nullptr;
}

ON_RenderContent& ON_RenderContent::CImpl::TopLevel(void)
{
  if (nullptr != m_parent)
  {
    return m_parent->m_impl->TopLevel();
  }

  return m_render_content;
}

bool ON_RenderContent::CImpl::ChangeChild(ON_RenderContent* old_child, ON_RenderContent* new_child)
{
  if (nullptr == old_child)
    return false;

  if (old_child == m_first_child)
  {
    if (nullptr != new_child)
    {
      m_first_child = new_child;
    }
    else
    {
      m_first_child = old_child->m_impl->m_next_sibling;
    }
  }
  else
  {
    const ON_RenderContent* prev_sibling = FindPrevSibling(old_child);
    if (nullptr == prev_sibling)
      return false;

    if (nullptr != new_child)
    {
      prev_sibling->m_impl->m_next_sibling = new_child;
    }
    else
    {
      prev_sibling->m_impl->m_next_sibling = old_child->m_impl->m_next_sibling;
    }
  }

  if (nullptr != new_child)
  {
    new_child->m_impl->m_next_sibling = old_child->m_impl->m_next_sibling;
    new_child->m_impl->m_parent = old_child->m_impl->m_parent;
  }

  delete old_child;

  return true;
}

ON_RenderContent* ON_RenderContent::CImpl::FindChild(const wchar_t* child_slot_name) const
{
  std::lock_guard<std::recursive_mutex> lg(m_mutex);

  ON_RenderContent* child_rc = m_first_child;
  while (nullptr != child_rc)
  {
    if (child_rc->ChildSlotName() == child_slot_name)
      return child_rc;

    child_rc = child_rc->m_impl->m_next_sibling;
  }

  return nullptr;
}

bool ON_RenderContent::CImpl::SetChild(ON_RenderContent* child, const wchar_t* child_slot_name)
{
  std::lock_guard<std::recursive_mutex> lg(m_mutex);

  if (nullptr != child)
  {
    if (nullptr != child->m_impl->m_model)
      return false;

    if (nullptr != child->m_impl->m_parent)
      return false;

    if ((nullptr == child_slot_name) || (0 == child_slot_name[0]))
      return false;

    child->m_impl->SetPropertyValue(ON_CHILD_SLOT_NAME, child_slot_name);
  }

  // Get any existing child with the same child slot name (may be null).
  auto* existing_child = FindChild(child_slot_name);
  if (nullptr != existing_child)
  {
    // There is an existing child with the same child slot name; replace it.
    if (!ChangeChild(existing_child, child)) // Deletes existing_child.
      return false;
  }
  else
  {
    // No existing child; just add the new one.
    if (nullptr != child)
    {
      if (!AddChild(*child))
        return false;
    }
  }

  if (nullptr != child)
  {
    auto* pModel = TopLevel().m_impl->m_model;
    child->m_impl->m_model = pModel;
  }

  return true;
}

void SetRenderContentNodeRecursive(const ON_RenderContent& rc, ON_XMLNode& node)
{
  // Copy the component name to the XML instance name.
  rc.m_impl->SetPropertyValue(ON_INSTANCE_NAME, rc.Name());

  // Copy the component id to the XML instance id.
  rc.m_impl->SetPropertyValue(ON_INSTANCE_ID, rc.Id());

  auto* child_node = new ON_XMLNode(rc.XMLNode());
  node.AttachChildNode(child_node);

  auto it = rc.GetChildIterator();
  ON_RenderContent* child_rc;
  while (nullptr != (child_rc = it.GetNextChild()))
  {
    SetRenderContentNodeRecursive(*child_rc, *child_node);
  }
}

static void BuildXMLHierarchy(const ON_RenderContent& rc, ON_XMLNode& node)
{
  // Recursively builds 'node' from the tree structure of the XML nodes in 'rc' and its children.

  node = rc.m_impl->m_node;

  auto* child_rc = rc.m_impl->m_first_child;
  while (nullptr != child_rc)
  {
    auto* child_node = new ON_XMLNode(L"");
    BuildXMLHierarchy(*child_rc, *child_node);
    node.AttachChildNode(child_node);

    child_rc = child_rc->m_impl->m_next_sibling;
  }
}

ON_VIRTUAL_OBJECT_IMPLEMENT(ON_RenderContent, ON_ModelComponent, "A98DEDDA-E4FA-4E1E-9BD3-2A0695C6D4E9");

ON_RenderContent::ON_RenderContent(const wchar_t* kind)
  :
  ON_ModelComponent(ON_ModelComponent::Type::RenderContent)
{
  m_impl = new (m_Impl) CImpl(*this, kind);

  // Set a unique instance id.
  ON_UUID uuid;
  ON_CreateUuid(uuid);
  SetId(uuid);

  // Set the plug-in id to the RDK plug-in id.
  m_impl->InternalSetPropertyValue(ON_PLUG_IN_ID, RdkPlugInId());

  // Set the render engine id to 'universal'.
  m_impl->InternalSetPropertyValue(ON_RENDER_ENGINE_ID, UniversalRenderEngineId());
}

ON_RenderContent::ON_RenderContent(const ON_RenderContent& rc)
  :
  ON_ModelComponent(ON_ModelComponent::Type::RenderContent, rc)
{
  m_impl = new (m_Impl) CImpl(*this, L"");
  operator = (rc);
}

ON_RenderContent::~ON_RenderContent()
{
  m_impl->~CImpl();
  m_impl = nullptr;
}

const ON_RenderContent& ON_RenderContent::operator = (const ON_RenderContent& rc)
{
  if (this != &rc)
  {
    ON_XMLRootNode root;
    BuildXMLHierarchy(rc, root);
    m_impl->SetXMLNode(root);
  }

  return *this;
}

ON_wString ON_RenderContent::TypeName(void) const
{
  return m_impl->GetPropertyValue(ON_TYPE_NAME).AsString();
}

void ON_RenderContent::SetTypeName(const wchar_t* name)
{
  m_impl->SetPropertyValue(ON_TYPE_NAME, name);
}

ON_wString ON_RenderContent::Notes(void) const
{
  return m_impl->GetPropertyValue(ON_NOTES).AsString();
}

void ON_RenderContent::SetNotes(const wchar_t* notes)
{
  m_impl->SetPropertyValue(ON_NOTES, notes);
}

ON_wString ON_RenderContent::Tags(void) const
{
  return m_impl->GetPropertyValue(ON_TAGS).AsString();
}

void ON_RenderContent::SetTags(const wchar_t* tags)
{
  m_impl->SetPropertyValue(ON_TAGS, tags);
}

ON_UUID ON_RenderContent::TypeId(void) const
{
  return m_impl->GetPropertyValue(ON_TYPE_ID).AsUuid();
}

void ON_RenderContent::SetTypeId(const ON_UUID& uuid)
{
  m_impl->SetPropertyValue(ON_TYPE_ID, uuid);
}

ON_UUID ON_RenderContent::RenderEngineId(void) const
{
  return m_impl->GetPropertyValue(ON_RENDER_ENGINE_ID).AsUuid();
}

void ON_RenderContent::SetRenderEngineId(const ON_UUID& uuid)
{
  m_impl->SetPropertyValue(ON_RENDER_ENGINE_ID, uuid);
}

ON_UUID ON_RenderContent::PlugInId(void) const
{
  return m_impl->GetPropertyValue(ON_PLUG_IN_ID).AsUuid();
}

void ON_RenderContent::SetPlugInId(const ON_UUID& uuid)
{
  m_impl->SetPropertyValue(ON_PLUG_IN_ID, uuid);
}

ON_UUID ON_RenderContent::GroupId(void) const
{
  return m_impl->GetPropertyValue(ON_GROUP_ID).AsUuid();
}

void ON_RenderContent::SetGroupId(const ON_UUID& group)
{
  m_impl->SetPropertyValue(ON_GROUP_ID, group);
}

bool ON_RenderContent::Hidden(void) const
{
  return m_impl->GetPropertyValue(ON_HIDDEN).AsBool();
}

void ON_RenderContent::SetHidden(bool hidden)
{
  m_impl->SetPropertyValue(ON_HIDDEN, hidden);
}

bool ON_RenderContent::Reference(void) const
{
  return m_impl->GetPropertyValue(ON_REFERENCE).AsBool();
}

void ON_RenderContent::SetReference(bool ref)
{
  m_impl->SetPropertyValue(ON_REFERENCE, ref);
}

bool ON_RenderContent::AutoDelete(void) const
{
  return m_impl->GetPropertyValue(ON_AUTO_DELETE).AsBool();
}

void ON_RenderContent::SetAutoDelete(bool autodel)
{
  m_impl->SetPropertyValue(ON_AUTO_DELETE, autodel);
}

ON_XMLVariant ON_RenderContent::GetParameter(const wchar_t* name) const
{
  std::lock_guard<std::recursive_mutex> lg(m_impl->m_mutex);

  ON_XMLVariant value;
  value.SetNull();

  // Try to get the new V8 parameter section.
  const ON_XMLNode* node = m_impl->m_node.GetNamedChild(ON_PARAMETERS_V8);
  if (nullptr != node)
  {
    // Got it, so use the new ON_XMLParametersV8 to get the parameter's value.
    ON_XMLParametersV8 p(*node);
    p.GetParam(name, value);
  }
  else
  {
    // Either no V8 section was found or the parameter isn't there yet.
    // Try to get the legacy parameter section. This should not fail.
    node = m_impl->m_node.GetNamedChild(ON_PARAMETERS);
    if (nullptr != node)
    {
      // Got it, so use the legacy ON_XMLParameters to get the parameter's value.
      ON_XMLParameters p(*node);
      p.GetParam(name, value);
    }
  }

  return value;
}

bool ON_RenderContent::SetParameter(const wchar_t* name, const ON_XMLVariant& value)
{
  std::lock_guard<std::recursive_mutex> lg(m_impl->m_mutex);

  bool success = false;

  // Create / get the new V8 parameter section.
  auto* node = m_impl->m_node.CreateNodeAtPath(ON_PARAMETERS_V8);
  if (nullptr != node)
  {
    // Use the new ON_XMLParametersV8 to write the parameter's value.
    ON_XMLParametersV8 p(*node);
    if (nullptr != p.SetParam(name, value))
      success = true;
  }

  // Create / get the legacy parameter section.
  node = m_impl->m_node.CreateNodeAtPath(ON_PARAMETERS);
  if (nullptr != node)
  {
    // Use the legacy ON_XMLParameters to write the parameter's value.
    ON_XMLParameters p(*node);
    if (nullptr != p.SetParam(name, value))
      success = true;
  }

  return success;
}

ON_RenderContent::ChildIterator ON_RenderContent::GetChildIterator(void) const
{
  return ChildIterator(this);
}

const ON_RenderContent* ON_RenderContent::Parent(void) const
{
  return m_impl->m_parent;
}

const ON_RenderContent* ON_RenderContent::FirstChild(void) const
{
  return m_impl->m_first_child;
}

const ON_RenderContent* ON_RenderContent::NextSibling(void) const
{
  return m_impl->m_next_sibling;
}

const ON_RenderContent& ON_RenderContent::TopLevel(void) const
{
  return m_impl->TopLevel();
}

bool ON_RenderContent::IsTopLevel(void) const
{
	return nullptr == m_impl->m_parent;
}

bool ON_RenderContent::IsChild(void) const
{
	return nullptr != m_impl->m_parent;
}

bool ON_RenderContent::SetChild(const ON_RenderContent& child, const wchar_t* child_slot_name)
{
  return m_impl->SetChild(child.Duplicate(), child_slot_name);
}

bool ON_RenderContent::DeleteChild(const wchar_t* child_slot_name)
{
  return m_impl->SetChild(nullptr, child_slot_name);
}

ON_wString ON_RenderContent::ChildSlotName(void) const
{
  return m_impl->GetPropertyValue(ON_CHILD_SLOT_NAME).AsString();
}

void ON_RenderContent::SetChildSlotName(const wchar_t* csn)
{
  m_impl->SetPropertyValue(ON_CHILD_SLOT_NAME, csn);
}

bool ON_RenderContent::ChildSlotOn(const wchar_t* child_slot_name) const
{
  const auto s = ON_wString(child_slot_name) + L"-" ON_MAT_POSTFIX_ON;
  return GetParameter(s).AsBool();
}

bool ON_RenderContent::SetChildSlotOn(bool on, const wchar_t* child_slot_name)
{
  const auto s = ON_wString(child_slot_name) + L"-" ON_MAT_POSTFIX_ON;
  return SetParameter(s, on);
}

const ON_RenderContent* ON_RenderContent::FindChild(const wchar_t* child_slot_name) const
{
  return m_impl->FindChild(child_slot_name);
}

static ON_XMLNode* NewXMLNodeRecursive(const ON_RenderContent& rc)
{
  ON_XMLNode* node = new ON_XMLNode(rc.m_impl->m_node);

  ON_RenderContent* child_rc = rc.m_impl->m_first_child;
  while (nullptr != child_rc)
  {
    ON_XMLNode* child_node = NewXMLNodeRecursive(*child_rc);
    if (nullptr != child_node)
    {
      node->AttachChildNode(child_node);
    }

    child_rc = child_rc->m_impl->m_next_sibling;
  }

  return node;
}

ON_wString ON_RenderContent::XML(bool recursive) const
{
  ON_XMLNode* node = &m_impl->m_node;

  if (recursive)
  {
    node = NewXMLNodeRecursive(*this);
  }

  const ON__UINT32 logical_count = node->WriteToStream(nullptr, 0);
  auto* stream = new wchar_t[size_t(logical_count) + 1];
  node->WriteToStream(stream, logical_count);
  stream[logical_count] = 0;
  const ON_wString xml = stream;
  delete[] stream;

  if (recursive)
    delete node;

  return xml;
}

bool ON_RenderContent::SetXML(const wchar_t* xml)
{
  ON_XMLRootNode node;
  if (ON_XMLNode::ReadError == node.ReadFromStream(xml))
    return false;

  m_impl->SetXMLNode(node);

  return true;
}

const ON_XMLNode& ON_RenderContent::XMLNode(void) const
{
  return m_impl->m_node;
}

ON_wString ON_RenderContent::Kind(void) const
{
  return m_impl->m_node.TagName();
}

const ON_RenderContent* ON_RenderContent::FromModelComponentRef(const ON_ModelComponentReference& ref,
                                                                const ON_RenderContent* none_return_value) // Static.
{
  const auto* rc = ON_RenderContent::Cast(ref.ModelComponent());
  if (nullptr != rc)
    return rc;

  return none_return_value;
}

void* ON_RenderContent::EVF(const wchar_t* func, void* data)
{
  return nullptr;
}

// ON_RenderContent::ChildIterator

class ON_RenderContent::ChildIterator::CImpl final
{
public:
  ON_RenderContent* m_current = nullptr;
};

ON_RenderContent::ChildIterator::ChildIterator(const ON_RenderContent* parent_rc)
{
  m_impl = new CImpl;

  if (nullptr != parent_rc)
  {
    m_impl->m_current = parent_rc->m_impl->m_first_child;
  }
}

ON_RenderContent::ChildIterator::~ChildIterator()
{
  delete m_impl;
  m_impl = nullptr;
}

ON_RenderContent* ON_RenderContent::ChildIterator::GetNextChild(void)
{
  ON_RenderContent* rc = m_impl->m_current;
  if (nullptr != rc)
  {
    m_impl->m_current = rc->m_impl->m_next_sibling;
  }

  return rc;
}

void* ON_RenderContent::ChildIterator::EVF(const wchar_t*, void*)
{
  return nullptr;
}

void SetModel(const ON_RenderContent& rc, ONX_Model& model)
{
  rc.m_impl->m_model = &model;

  auto it = rc.GetChildIterator();
  ON_RenderContent* child_rc = nullptr;
  while (nullptr != (child_rc = it.GetNextChild()))
  {
    SetModel(*child_rc, model);
  }
}

ON_RenderContent* NewRenderContentFromNode(const ON_XMLNode& node)
{
  ON_RenderContent* rc = nullptr;

  const ON_wString& kind = node.TagName();

  if (ON_KIND_MATERIAL == kind)
    rc = new ON_RenderMaterial;
  else
  if (ON_KIND_ENVIRONMENT == kind)
    rc = new ON_RenderEnvironment;
  else
  if (ON_KIND_TEXTURE == kind)
    rc = new ON_RenderTexture;

  if (nullptr != rc)
  {
    rc->m_impl->SetXMLNode(node);
  }

  return rc;
}

// ON_RenderMaterial

ON_OBJECT_IMPLEMENT(ON_RenderMaterial, ON_RenderContent, "493E6601-F95B-4A5D-BB6F-2F6633076907");

ON_RenderMaterial::ON_RenderMaterial()
  :
  ON_RenderContent(ON_KIND_MATERIAL)
{
}

ON_RenderMaterial::ON_RenderMaterial(const ON_RenderMaterial& mat)
  :
  ON_RenderContent(mat)
{
}

ON_RenderMaterial::~ON_RenderMaterial()
{
}

void ON_RenderMaterial::operator = (const ON_RenderMaterial& mat)
{
  ON_RenderContent::operator = (mat);
}

ON_XMLVariant ParamHelper(const ON_XMLParameters& p, const wchar_t* name)
{
  ON_XMLVariant value;
  if (!p.GetParam(name, value))
    value = L"";

  return value;
}

ON_Material ON_RenderMaterial::SimulatedMaterial(void) const
{
  std::lock_guard<std::recursive_mutex> lg(m_impl->m_mutex);

  ON_Material mat;

  const ON_XMLNode* sim_node = m_impl->XMLNode_Simulation();
  if (nullptr != sim_node)
  {
    ON_XMLParameters p(*sim_node);

    mat.m_ambient               =       ParamHelper(p, ON_MAT_AMBIENT            ).AsColor();
    mat.m_diffuse               =       ParamHelper(p, ON_MAT_DIFFUSE            ).AsColor();
    mat.m_emission              =       ParamHelper(p, ON_MAT_EMISSION           ).AsColor();
    mat.m_specular              =       ParamHelper(p, ON_MAT_SPECULAR           ).AsColor();
    mat.m_reflection            =       ParamHelper(p, ON_MAT_REFLECTION         ).AsColor();
    mat.m_reflectivity          =       ParamHelper(p, ON_MAT_REFLECTIVITY_AMOUNT).AsDouble();
    mat.m_shine                 =       ParamHelper(p, ON_MAT_SHINE              ).AsDouble() * ON_Material::MaxShine;
    mat.m_transparency          =       ParamHelper(p, ON_MAT_TRANSPARENCY_AMOUNT).AsDouble();
    mat.m_index_of_refraction   =       ParamHelper(p, ON_MAT_IOR                ).AsDouble();
    mat.m_reflection_glossiness = 1.0 - ParamHelper(p, ON_MAT_POLISH_AMOUNT      ).AsDouble();
    mat.m_refraction_glossiness = 1.0 - ParamHelper(p, ON_MAT_CLARITY_AMOUNT     ).AsDouble();
    mat.m_transparent           =       ParamHelper(p, ON_MAT_TRANSPARENT        ).AsColor();
    mat.SetFresnelReflections   (       ParamHelper(p, ON_MAT_FRESNEL_ENABLED    ).AsBool());
    mat.SetDisableLighting      (       ParamHelper(p, ON_MAT_DISABLE_LIGHTING   ).AsBool());

    mat.m_fresnel_index_of_refraction = 1.56;

    if (ParamHelper(p, ON_MAT_IS_PHYSICALLY_BASED).AsBool())
    {
      mat.ToPhysicallyBased();

      auto pbm = mat.PhysicallyBased();

      auto brdf = ON_PhysicallyBasedMaterial::BRDFs::GGX;
      const ON_wString s = ParamHelper(p, ON_MAT_PBR_BRDF).AsString();
      if (s == ON_MAT_PBR_BRDF_WARD)
        brdf = ON_PhysicallyBasedMaterial::BRDFs::Ward;
      pbm->SetBRDF(brdf);

      pbm->SetBaseColor                 (ParamHelper(p, ON_MAT_PBR_BASE_COLOR).AsColor());
      pbm->SetSubsurface                (ParamHelper(p, ON_MAT_PBR_SUBSURFACE).AsDouble());
      pbm->SetSubsurfaceScatteringColor (ParamHelper(p, ON_MAT_PBR_SUBSURFACE_SCATTERING_COLOR).AsColor());
      pbm->SetSubsurfaceScatteringRadius(ParamHelper(p, ON_MAT_PBR_SUBSURFACE_SCATTERING_RADIUS).AsDouble());
      pbm->SetSpecular                  (ParamHelper(p, ON_MAT_PBR_SPECULAR).AsDouble());
      pbm->SetSpecularTint              (ParamHelper(p, ON_MAT_PBR_SPECULAR_TINT).AsDouble());
      pbm->SetMetallic                  (ParamHelper(p, ON_MAT_PBR_METALLIC).AsDouble());
      pbm->SetRoughness                 (ParamHelper(p, ON_MAT_PBR_ROUGHNESS).AsDouble());
      pbm->SetAnisotropic               (ParamHelper(p, ON_MAT_PBR_ANISOTROPIC).AsDouble());
      pbm->SetAnisotropicRotation       (ParamHelper(p, ON_MAT_PBR_ANISOTROPIC_ROTATION).AsDouble());
      pbm->SetSheen                     (ParamHelper(p, ON_MAT_PBR_SHEEN).AsDouble());
      pbm->SetSheenTint                 (ParamHelper(p, ON_MAT_PBR_SHEEN_TINT).AsDouble());
      pbm->SetClearcoat                 (ParamHelper(p, ON_MAT_PBR_CLEARCOAT).AsDouble());
      pbm->SetClearcoatRoughness        (ParamHelper(p, ON_MAT_PBR_CLEARCOAT_ROUGHNESS).AsDouble());
      pbm->SetOpacity                   (ParamHelper(p, ON_MAT_PBR_OPACITY).AsDouble());
      pbm->SetOpacityIOR                (ParamHelper(p, ON_MAT_PBR_OPACITY_IOR).AsDouble());
      pbm->SetOpacityRoughness          (ParamHelper(p, ON_MAT_PBR_OPACITY_ROUGHNESS).AsDouble());
      pbm->SetEmission                  (ParamHelper(p, ON_MAT_PBR_EMISSION_COLOR).AsColor());
      pbm->SetAlpha                     (ParamHelper(p, ON_MAT_PBR_ALPHA).AsDouble());
      pbm->SetUseBaseColorTextureAlphaForObjectAlphaTransparencyTexture(ParamHelper(p, ON_MAT_PBR_USE_BASE_COLOR_TEXTURE_ALPHA).AsBool());
    }

    mat.SetName(Name());

    mat.m_textures.Destroy();

    // Iterator over the children.
    int count = 1;
    while (true)
    {
      ON_Texture tex;
      ON_XMLVariant v;

      ON_wString s;
      s.Format(ON_MAT_TEXSIM_FORMAT, count);

      if (!p.GetParam(s + ON_MAT_TEXSIM_FILENAME, v))
        break; // Not ideal.

      tex.m_image_file_reference.SetFullPath(v.AsString(), false);

      if (p.GetParam(s + ON_MAT_TEXSIM_ON, v))
        tex.m_bOn = v;

      if (p.GetParam(s + ON_MAT_TEXSIM_AMOUNT, v))
        tex.m_blend_constant_A = v;

      if (p.GetParam(s + ON_MAT_TEXSIM_TYPE, v))
        tex.m_type = ON_Texture::TYPE(v.AsInteger());

      if (p.GetParam(s + ON_MAT_TEXSIM_FILTER, v))
        tex.m_minfilter = tex.m_magfilter = ON_Texture::FILTER(v.AsInteger());

      if (p.GetParam(s + ON_MAT_TEXSIM_MODE, v))
        tex.m_mode = ON_Texture::MODE(v.AsInteger());

      if (p.GetParam(s + ON_MAT_TEXSIM_UVW, v))
        tex.m_uvw = v.AsXform();

      if (p.GetParam(s + ON_MAT_TEXSIM_WRAP_U, v))
        tex.m_wrapu = ON_Texture::WRAP(v.AsInteger());

      if (p.GetParam(s + ON_MAT_TEXSIM_WRAP_V, v))
        tex.m_wrapv = ON_Texture::WRAP(v.AsInteger());

      mat.m_textures.Append(tex);
      count++;
    }
  }

  return mat;
}

// ON_RenderEnvironment

ON_OBJECT_IMPLEMENT(ON_RenderEnvironment, ON_RenderContent, "A0AB8EF9-5FD4-4320-BBDA-A1200D1846E4");

ON_RenderEnvironment::ON_RenderEnvironment()
  :
  ON_RenderContent(ON_KIND_ENVIRONMENT)
{
}

ON_RenderEnvironment::ON_RenderEnvironment(const ON_RenderEnvironment& env)
  :
  ON_RenderContent(env)
{
}

ON_RenderEnvironment::~ON_RenderEnvironment()
{
}

void ON_RenderEnvironment::operator = (const ON_RenderEnvironment& env)
{
}

ON_Environment ON_RenderEnvironment::SimulatedEnvironment(void) const
{
  std::lock_guard<std::recursive_mutex> lg(m_impl->m_mutex);

  ON_Environment env;

  const ON_XMLNode* sim_node = m_impl->XMLNode_Simulation();
  if (nullptr != sim_node)
  {
    ON_XMLVariant v;
    ON_XMLParameters p(*sim_node);

    if (p.GetParam(ON_ENVSIM_BACKGROUND_COLOR, v))
      env.SetBackgroundColor(v.AsColor());

    if (p.GetParam(ON_ENVSIM_BACKGROUND_IMAGE, v))
    {
      ON_Texture tex;
      tex.m_image_file_reference.SetFullPath(v.AsString(), false);
      // TODO: What other ON_Texture params need to be set?
      env.SetBackgroundImage(tex);
    }

    if (p.GetParam(ON_ENVSIM_BACKGROUND_PROJECTION, v))
    {
      const auto proj = ON_Environment::ProjectionFromString(v.AsString());
      env.SetBackgroundProjection(proj);
    }
  }

  return env;
}

// ON_RenderTexture

ON_OBJECT_IMPLEMENT(ON_RenderTexture, ON_RenderContent, "677D9905-CC8C-41E6-A7AD-2409DDE68ED0");

ON_RenderTexture::ON_RenderTexture()
  :
  ON_RenderContent(ON_KIND_TEXTURE)
{
}

ON_RenderTexture::ON_RenderTexture(const ON_RenderTexture& tex)
  :
  ON_RenderContent(tex)
{
}

ON_RenderTexture::~ON_RenderTexture()
{
}

void ON_RenderTexture::operator = (const ON_RenderTexture& tex)
{
}

ON_Texture ON_RenderTexture::SimulatedTexture(void) const
{
  std::lock_guard<std::recursive_mutex> lg(m_impl->m_mutex);

  ON_Texture tex;

  const ON_XMLNode* sim_node = m_impl->XMLNode_Simulation();
  if (nullptr != sim_node)
  {
    ON_XMLVariant v;
    ON_XMLParameters p(*sim_node);

    if (p.GetParam(ON_TEXSIM_FILENAME, v))
    {
      tex.m_image_file_reference.SetFullPath(v.AsString(), false);
    }

    if (p.GetParam(ON_TEXSIM_OFFSET, v))
    {
      XF xf;
      ON_DeconstructXform(tex.m_uvw, xf);
      const auto pt = v.As2dPoint();
      xf.trans_x = pt[0];
      xf.trans_y = pt[1];
      ON_ConstructXform(xf, tex.m_uvw);
    }

    if (p.GetParam(ON_TEXSIM_REPEAT, v))
    {
      XF xf;
      ON_DeconstructXform(tex.m_uvw, xf);
      const auto pt = v.As2dPoint();
      xf.scale_x = pt[0];
      xf.scale_y = pt[1];
      ON_ConstructXform(xf, tex.m_uvw);
    }

    if (p.GetParam(ON_TEXSIM_ROTATION, v))
    {
      XF xf;
      ON_DeconstructXform(tex.m_uvw, xf);
      xf.angle_z = v.AsDouble();
      ON_ConstructXform(xf, tex.m_uvw);
    }

    if (p.GetParam(ON_TEXSIM_WRAP_TYPE, v))
    {
      const auto wt = ON_Texture::WRAP(v.AsInteger());
      tex.m_wrapu = wt;
      tex.m_wrapv = wt;
      tex.m_wrapw = wt;
    }

    if (p.GetParam(ON_TEXSIM_MAPPING_CHANNEL, v))
    {
      tex.m_mapping_channel_id = v.AsInteger();
    }
  }

  return tex;
}

int ONX_Model::AddRenderMaterial(const wchar_t* mat_name)
{
  static ON_UUID uuidPB = { 0x5a8d7b9b, 0xcdc9, 0x49de, { 0x8c, 0x16, 0x2e, 0xf6, 0x4f, 0xb0, 0x97, 0xab } };

  ON_RenderMaterial mat;
  mat.SetTypeId(uuidPB);

  const ON_wString unused_name = m_manifest.UnusedName(mat.ComponentType(), ON_nil_uuid, mat_name, nullptr, nullptr, 0, nullptr);
  mat.SetName(unused_name);

  const ON_ModelComponentReference mcr = AddModelComponent(mat, true);
  const auto* model_mat = ON_RenderMaterial::Cast(mcr.ModelComponent());
  if (nullptr == model_mat)
  {
    ON_ERROR("Failed to add render material; AddModelComponent() failed");
    return ON_UNSET_INT_INDEX;
  }

  return model_mat->Index();
}

int ONX_Model::AddRenderEnvironment(const wchar_t* env_name)
{
  static ON_UUID uuidBE = { 0xba51ce00, 0xba51, 0xce00, { 0xba, 0x51, 0xce, 0xba, 0x51, 0xce, 0x00, 0x00 } };

  ON_RenderEnvironment env;
  env.SetTypeId(uuidBE);

  const ON_wString unused_name = m_manifest.UnusedName(env.ComponentType(), ON_nil_uuid, env_name, nullptr, nullptr, 0, nullptr);
  env.SetName(unused_name);

  const ON_ModelComponentReference mcr = AddModelComponent(env, true);
  const auto* model_env = ON_RenderEnvironment::Cast(mcr.ModelComponent());
  if (nullptr == model_env)
  {
    ON_ERROR("Failed to add render environment; AddModelComponent() failed");
    return ON_UNSET_INT_INDEX;
  }

  return model_env->Index();
}

int ONX_Model::AddRenderTexture(const wchar_t* fn)
{
  static const ON_UUID uuidBM = { 0x57e0ed08, 0x1907, 0x4529, { 0xb0, 0x1b, 0x0c, 0x4a, 0x24, 0x24, 0x55, 0xfd } };

  const auto filename = ON_FileSystemPath::CleanPath(fn);

  if (!ON_FileSystem::PathExists(filename))
  {
    ON_ERROR("Failed to add render texture; file does not exist");
    return ON_UNSET_INT_INDEX;
  }

  ON_RenderTexture tex;
  tex.SetTypeId(uuidBM);
  tex.SetParameter(ON_TEX_FILENAME, filename);

  const ON_wString tex_name = ON_FileSystemPath::FileNameFromPath(filename, false);
  tex.SetName(tex_name);

  const ON_wString unused_name = m_manifest.UnusedName(tex.ComponentType(), ON_nil_uuid, tex_name, nullptr, nullptr, 0, nullptr);
  tex.SetName(unused_name);

  const ON_ModelComponentReference mcr = AddModelComponent(tex, true);
  const auto* model_tex = ON_RenderTexture::Cast(mcr.ModelComponent());
  if (nullptr == model_tex)
  {
    ON_ERROR("Failed to add render texture; AddModelComponent() failed");

    return ON_UNSET_INT_INDEX;
  }

  return model_tex->Index();
}
